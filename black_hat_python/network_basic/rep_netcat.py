"""
file: bhnet.py
language: python 2
book: Black Hat Python - Justin Seitz

Black hat python netcat replacement,
allows file upload,
gives access to command line

functions:
main(): checks options and then listens or sends data
usage() : has usage details, documentation folder
client_sender(): to send data to the server
server_loop(): listens for reqs
client_handler(): file uploads, command execution
run_command(): runs the command and sends the output back
"""

import sys
import socket
import getopt
import threading
import subprocess

# global variables
LISTEN = False
COMMAND = False
UPLOAD = False
EXECUTE = ""
TARGET = ""
UPLOAD_DESTINATION = ""
PORT = 0

def usage():
    print "BHP Net Tool"
    print "Usage: bhpnet.py -t target_host -p port"


def server_loop():
    global TARGET
    
    # if no target is defined, we listen on all interfaces
    if not len(TARGET):

        TARGET = "0.0.0.0"
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((TARGET,PORT))
    server.listen(5)
    
    while True:
        
        client_socket, addr = server.accept()
        # spin off a thread to handle our new client
        client_thread = threading.Thread(target=client_handler,
                args=(client_socket,))
        client_thread.start()


def run_command(command):
        # trim the newline
        command = command.rstrip()
        # run the command and get the output back
        try:
             output = subprocess.check_output(command,stderr=subprocess.STDOUT, shell=True)
        except Exception, e:
            output = "Failed to execute command." + str(e) + "\r\n"
            # send the output back to the client
        
        return output


def client_handler(client_socket):
    global UPLOAD
    global EXECUTE
    global COMMAND
    
    # check for upload
    if len(UPLOAD_DESTINATION):
        
        # read in all of the bytes and write to our destination
        file_buffer = ""
        
        # keep reading data until none is available
        while True:
            data = client_socket.recv(1024)

            if not data:
                break
            else:
                file_buffer += data
                
        # now we take these bytes and try to write them out
        try:
            file_descriptor = open(UPLOAD_DESTINATION,"wb")
            file_descriptor.write(file_buffer)
            file_descriptor.close()
            # acknowledge that we wrote the file out
            client_socket.send("Successfully saved file to %s\r\n" % UPLOAD_DESTINATION)
        except:
            client_socket.send("Failed to save file to %s\r\n" % UPLOAD_DESTINATION)

    # check for command execution
    if len(EXECUTE):
        # run the command
        output = run_command(EXECUTE)
        client_socket.send(output)
    
    # now we go into another loop if a command shell was requested
    if COMMAND:
        while True:
            # show a simple prompt
            client_socket.send("<BHP:#> ")
            # now we receive until we see a linefeed (enter key)
            cmd_buffer = ""
            while "\n" not in cmd_buffer:
                cmd_buffer += client_socket.recv(1024)
            
            # send back the command output
            response = run_command(cmd_buffer)
            # send back the response
            client_socket.send(response)


def client_sender(buffer):
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        client.connect((TARGET,PORT))

        if len(buffer):
            client.send(buffer)


        while True:

            recv_len = 1
            response = ""

            while recv_len:

                data = client.recv(4096)
                recv_len = len(data)
                response += data

                if recv_len < 4096:
                    break
            
            print response,

            # more input
            buffer = raw_input("")
            buffer += "\n"

            client.send(buffer)

    except Exception, e:
        print "[*] Exception! Exiting."+str(e)
        client.close()


def main():
    global LISTEN
    global PORT
    global EXECUTE
    global COMMAND
    global UPLOAD_DESTINATION
    global TARGET

    if not len(sys.argv[1:]):
        usage()

    # reading the cmd options
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hle:t:p:cu:",
                ["help","listen","execute","target","port","command","upload"])
    except getopt.GetoptError as err:
        print str(err)
        usage()

    for o,a in opts:
        if o in ("-h"):
            usage()
        elif o in ("-l"):
            LISTEN = True
        elif o in ("-e"):
            EXECUTE = a
        elif o in ("-t"):
            TARGET = a
        elif o in ("-p"):
            PORT = int(a)
        elif o in ("-c"):
            COMMAND = True
        elif o in ("-u"):
            UPLOAD_DESTINATION = a
        elif o in ("-p"):
            port = int(a)
        else:
            assert False, "Unhandled option"

    # listening or sending
    if not LISTEN and len(TARGET) and PORT > 0:
        # read in the bugger
        buffer = sys.stdin.read()

        client_sender(buffer)

    if LISTEN:
        server_loop()

main()

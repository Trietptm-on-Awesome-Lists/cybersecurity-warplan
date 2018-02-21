#!/bin/bash


#
echo "Parameters"
# $0 file path
# $1 BASEURL
# $2 PORT
# $3 Connection Type TCP|UDP
# $4 Timeout

BASEURL=$1
PORT=$2
echo "BASEURL "$BASEURL
echo "PORT "$PORT
##############

URL=$BASEURL/$PORT


# CONRES= $(echo >/dev/tcp/www.google.com/80) &>/dev/null
# if [[ $CONRES == 0 ]]; then
#     echo "Connected"
# else
#     echo "Fail"
# fi


exec 3<>/dev/tcp/$URL
echo "Connection established with "$BASEURL". ADD REQUEST HERE:"
# read USER_REQ
# echo -e $USER_REQ 1>&5
echo -e "HEAD / HTTP/1.1 \n" 1>&3
RESPONSE="$(cat <&3)"

if [ "X$RESPONSE" = "X0" ]; then
echo "Connection successful. Exit code: $RESPONSE"
else
echo "Connection unsuccessful. Exit code: $RESPONSE"
fi

# echo $RESPONSE



exec 5<>/dev/udp/$URL
echo -e "GET / HTTP/1.0\n" 1>&5
response="$(cat <&5)"
echo $response

if [ "X$MYEXIT" = "X0" ]; then
  echo "Connection successful. Exit code: $MYEXIT"
else
  echo "Connection unsuccessful. Exit code: $MYEXIT"
fi

exit $MYEXIT

REQUEST=$(cat </dev/tcp/$URL)
RESPONSE=$(echo "$REQUEST")# | awk '{print$3}')   # Third field is UTC (GMT) time.
# Exercise: modify this for different time zones.

echo $RESPONSE

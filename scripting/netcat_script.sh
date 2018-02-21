#!/bin/bash


# echo "Parameters"
# $0 file path
# $1 BASEURL
# $2 PORT
# $3 Connection Type TCP|UDP
# $4 Timeout

#
# READ USER OPTIONS
#
while getopts ":h" opt; do
  case $opt in
    h)
      echo "Follow this format [./netcat_script {ip_address} {port} {timer(default: 1)} {range}]" >&2
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      ;;
  esac
done


IF values are not set
if [ -z "${1}" ] || [ -z "${2}" ]; then
    echo "Baseurl and port are required. Follow this format [./netcat_script {ip_address} {port} {timer(default: 1)} ]"
    exit 0
fi

BASEURL=$1
PORT=$2
TIMEOUT=${3:-1}
RANGE=${4:-2}
SUBNET=${5:-"255.255.255.0"}
echo "BASEURL "$BASEURL
echo "PORT "$PORT
echo "TIMER "$TIMEOUT
echo "RANGE "$RANGE
echo "SUBNET "$SUBNET

IFS=. read -r i1 i2 i3 i4 <<< $BASEURL
IFS=. read -r m1 m2 m3 m4 <<< $SUBNET
VAL= $("%d.%d.%d.%d" "$((i1 & m1))" "$((i2 & m2))" "$((i3 & m3))" "$((i4 & m4))" 2>&1)
echo $VAL
while [[ $i -le $RANGE ]]
do
  RESPONSE= $(nc -zv -w2 $BASEURL$i 80)
  if [ "$RESPONSE" = 0 ]; then
    echo "SUCCESS"
  else
    echo "FAIL"
  fi
  ((i = i + 1))
done

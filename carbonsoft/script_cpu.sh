#!/bin/bash
if [ -n "$1" ]
then
rought_adress=$1
else
rought_adress="127.0.0.1:8001"
fi
user=$(whoami)
adress="$rought_adress/api/"
while true
do
mycpu=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')
curl -X POST -d "{\"user\": \"$user\", \"cpu\": $mycpu}" -H "Content-Type:application/json" $adress
sleep 10
done

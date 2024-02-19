#!/usr/bin/with-contenv bashio

MESSAGE=$(bashio::config 'message')
HOSTNAME=$(bashio::config 'hostName')

echo "option message \"${MESSAGE}\";"
echo "option hostName \"${HOSTNAME}\";"

#ping -c1 $HOSTNAME

python3 main.py

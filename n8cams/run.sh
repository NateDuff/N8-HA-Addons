#!/usr/bin/with-contenv bashio

MESSAGE=$(bashio::config 'message')

echo "option message \"${MESSAGE}\";"
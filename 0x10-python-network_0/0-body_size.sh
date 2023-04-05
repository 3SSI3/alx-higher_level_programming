#!/bin/bash
# Script that send a request to URL with curl, Displays the size of the body of the response
curl -s "$1" | wc -c

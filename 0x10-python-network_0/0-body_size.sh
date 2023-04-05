#!/bin/bash
# Send a request to URL with curl, Displays the size of the body of the response
read -p "Enter URL: " url
response=$(curl -s $url)
size=$(echo -n $response | wc -c)
echo "Response body size: $size bytes"

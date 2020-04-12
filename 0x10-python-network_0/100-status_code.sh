#!/bin/bash
# take a URL, send a request to that URL, and display the size of the body of the response
curl -s -o /dev/null -w "%{http_code}" "$1"

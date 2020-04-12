#!/bin/bash
# take a URL, send a request to that URL, and display the size of the body of the response
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"

#!/bin/bash
# take a URL, send a request to that URL, and display the size of the body of the response
curl -sL -XPUT -d user_id=98 -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me

#!/bin/bash
# script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response.


curl -s -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me --output /dev/null -w "You got me!%{http_code}\n" | grep -o "You got me!"


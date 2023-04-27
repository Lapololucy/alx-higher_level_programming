#!/bin/bash
# Curl body size
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2

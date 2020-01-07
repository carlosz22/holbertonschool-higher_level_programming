#!/bin/bash
# Get the HTTP code from an URL
curl -s -o /dev/null -w "%{http_code}" "$1"

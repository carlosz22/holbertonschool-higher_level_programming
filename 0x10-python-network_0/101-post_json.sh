#!/bin/bash
# GET request with a header
curl -s -X POST -H 'Content-Type: application/json' -d @"$2" "$1"

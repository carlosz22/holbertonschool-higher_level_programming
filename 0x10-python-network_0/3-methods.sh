#!/bin/bash
# Gets the size in bytes from an url
curl -sI "$1" | grep Allow | cut -d ":" -f 2 | cut -c 2-

#!/bin/bash
# rthr het hy
curl -sX OPTIONS -I "$1" | grep Allow | cut -d " " -f 2-

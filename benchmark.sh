
# benchmark file

#!/bin/bash
SERVER_HOST=http://localhost:5000
CONCURRENT_T=100
COUNT_T=1000

# check if apache benchmark exists
command -v ab >/dev/null 2>&1  -n $COUNT_T -c $CONCURRENT_T $SERVER_HOST/cricinfo || { echo >&2 "I require apache benchmark but it's not installed.  Aborting."; exit 1; }

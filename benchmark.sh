
# benchmark file

#!/bin/bash

# check if apache benchmark exists
command -v ab >/dev/null 2>&1  -n 1000 -c 100 http://localhost:5000/cricinfo || { echo >&2 "I require apache benchmark but it's not installed.  Aborting."; exit 1; }

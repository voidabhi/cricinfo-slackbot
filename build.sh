
set -e 

# check if make is installed
command -v make >/dev/null 2>&1 || { echo >&2 "I require make but it's not installed.  Aborting."; exit 1; }

make install

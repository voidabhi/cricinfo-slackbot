

# check if procfile exists
file_exists=test -e "Procfile"

# run make
make .

# check if heroku branch exists
remote_exists=`git show-ref refs/heads/heroku`

# push if file and remote exists
if [ "$file_exists" & "$remote_exists" ]; then
    # push to heroku
    git push heroku master
fi

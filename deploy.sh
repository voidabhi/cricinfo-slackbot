

# check if procfile exists
file_exists=test -e "$file_name"

# check if heroku branch exists
remote_exists=`git show-ref refs/heads/heroku`
if [ "$file_exists" & "$remote_exists" ]; then
    # push to heroku
    git push heroku master
fi

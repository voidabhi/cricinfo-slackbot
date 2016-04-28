#!/usr/bin/python

import os
import requests
from flask import Flask, request, abort
from cricinfo import Cricinfo

IN_TOKEN = os.getenv("IN_TOKEN", "YOUR_IN_TOKEN")
OUT_TOKEN = os.getenv("OUT_TOKEN", "YOUR_OUT_TOKEN")

app = Flask(__name__)
c = Cricinfo()

def post_message(token, channel, text, username):
    URL = "https://slack.com/api"
    CHAT_POST = "chat.postMessage"
    params = {
        "token": token,
        "channel": channel,
        "text": text,
        "username": username,
    }
    return requests.post("{}/{}".format(URL, CHAT_POST), data=params)

@app.route("/cricinfo", methods=["POST"])
def cricinfo():
    # validate required arguments
    try:
        in_token = request.form["token"]
        channel = request.form["channel_id"]
        text = request.form["text"]
        username = request.form["user_name"]
    except:
        abort(400)
    if in_token != IN_TOKEN:
        abort(401)
    
    # create message from template
    tpl = """
        ```
            %s
        ```
    """%(str(c.matches()))
    # print 'request'
    # r = post_message(OUT_TOKEN, channel, t, username)
    # if r.status_code != 200:
    #     abort(500)
    
    # send message
    return tpl

if __name__ == "__main__":
    app.run()

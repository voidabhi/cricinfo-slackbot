

import os
import random
import requests
from flask import Flask, request, abort
from cricinfo import cricinfo

URL = "https://slack.com/api"
CHAT_POST = "chat.postMessage"
INTENSITY = { "up": 5, "mid": 5, "down": 5}
IN_TOKEN = os.getenv("IN_TOKEN", "")
OUT_TOKEN = os.getenv("OUT_TOKEN", "")

app = Flask(__name__)

@app.route("/cricinfo", methods=["POST"])
def cricinfo():
    try:
        in_token = request.form["token"]
        channel = request.form["channel_id"]
        text = request.form["text"]
        username = request.form["user_name"]
    except:
        abort(400)
    if in_token != IN_TOKEN:
        abort(401)
    update = cricinfo(text, INTENSITY)
    params = {
        "token": OUT_TOKEN,
        "channel": channel,
        "text": update,
        "username": username,
    }
    r = requests.post("{}/{}".format(URL, CHAT_POST), data=params)
    if r.status_code != 200:
        abort(500)

    c = __doc__.split("\n")
    random.shuffle(c)
    return c[0]

if __name__ == "__main__":
    app.run()

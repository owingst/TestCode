#!/usr/bin/env python3
""" TestPush Module """
# -*- coding: utf-8 -*-
# =============================================================================
# Title           : testpush.py
# Description     : This script handles push notification testing
# Created By      : Tim Owings
# Created Date    : Jan 17, 2022
# Python          : 3.9.2
# =============================================================================
import subprocess
import sys
import json

def push(token, pushtopic, certfile):
    """ Send Push Notifications """

    msg = "Hi Tim"

    try:

        x = {"aps": {"alert": {"title": msg, "body": "WooHoo!"}, "sound": "Lucy-Im-home.aiff"}}
        jsonMsg = json.dumps(x)
        partUrl = "https://api.sandbox.push.apple.com/3/device/"

        tokenUrl = partUrl + token
        topic = "apns-topic: " + pushtopic

        rc = subprocess.check_output(["curl", "-v", "--header", topic,  "--header", "apns-push-type: alert",
                                        "--cert", certfile, "--key-type", "PEM", "--data", jsonMsg, "--http2",  tokenUrl])

        rc = rc.decode("utf-8")

        if (rc):
                print("push: call failed: rc =  {}\n".format(rc))

        else:
                print("push: call was successful \n")

    except Exception as e:
        print("push: Exception is {}\n".format(e))
                
if __name__ == "__main__":
    push(sys.argv[1], sys.argv[2], sys.argv[3])

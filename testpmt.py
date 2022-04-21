#!/usr/bin/env python3
""" testpmt Module """
# -*- coding: utf-8 -*-
# =============================================================================
# Title           : """ testpmt Module """
# Description     : This script handles testing of getPMTDataByDate
# Created By      : Tim Owings
# Created Date    : Apr 21, 2022
# Python          : 3.9.2
# =============================================================================
import json
import time
import os
import sys
import datetime
import requests
from _datetime import timedelta


def getPMTData():

    now = datetime.datetime.now()
    dt = datetime.datetime.now() - datetime.timedelta(hours = 8)

    print("now is {}\n".format(now))
    print("dt is {}\n".format(dt))

    r = requests.get("http://192.168.1.74:5000/getPMTDataByDate", params={'start': dt, 'end': now})

    if (r.status_code == 200):

        print("main: request was successful!")
        #print("r.json is {}\n".format(r.json()))
        data = r.json()
        for x in data:
            print("x is {}\n".format(x))
        
    else:
        print("main: Request Failed! status code {}".format(r.status_code))  

def main():
    
    getPMTData()

if __name__ == "__main__":
    main()
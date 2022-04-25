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
import io
import sys
import datetime
import requests
from _datetime import timedelta
from matplotlib import pyplot as plt
from PIL import Image
from io import BytesIO

#@app.route('/getPMTData', methods=['GET']) 
def getPMTData():
    
    dataArray = []

    r = requests.get("http://192.168.1.74:5000/getPMTData")

    if (r.status_code == 200):

        print("getPMTData: request was successful!\n")
        resp = r.json()

        print("getPMTData: data returned is {}\n".format(resp))
        return resp

    else:
        print("getPMTData: Request Failed! status code {}".format(r.status_code))


def getPMTDataByDate():
    
    dataArray = []

    end = datetime.datetime.now() - datetime.timedelta(hours = 24)
    start = end - datetime.timedelta(hours = 8)

    print("getPMTDataByDate: start {} and end {} dates: \n".format(start, end)) 

    r = requests.get("http://192.168.1.74:5000/getPMTDataByDate", params={'start': start, 'end': end})

    if (r.status_code == 200):

        print("getPMTDataByDate: request was successful!\n")
        resp = r.json()

        for x in resp:
            print("x is {}\n".format(x))
        #return resp

    else:
        print("getPMTDataByDate: Request Failed! status code {}".format(r.status_code))

       
def getPMTPlotByDate():
    
    dataArray = []

    # end = datetime.datetime.now() - datetime.timedelta(hours = 24)
    # start = end - datetime.timedelta(hours = 8)
    end = datetime.datetime.now()
    start = end - datetime.timedelta(hours = 24)

    r = requests.get("http://192.168.1.74:5000/getPMTPlotByDate", params={'start': start, 'end': end})

    if (r.status_code == 200):

        print("getPMTPlotData: request was successful!\n")
        img = Image.open(BytesIO(r.content)) 
        img.show()

    else:
        print("getPMTPlotData: Request Failed! status code {}".format(r.status_code))


def main():
    
    #getPMTData()
    #getPMTDataByDate()
    getPMTPlotByDate()

if __name__ == "__main__":
    main()
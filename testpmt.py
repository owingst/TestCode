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


def getPMTData():
    
    dataArray = []

    now = datetime.datetime.now()
    dt = datetime.datetime.now() - datetime.timedelta(hours = 8)

    r = requests.get("http://192.168.1.74:5000/getPMTDataByDate", params={'start': dt, 'end': now})

    if (r.status_code == 200):

        print("getPMTData: request was successful!\n")
        resp = r.json()

        for x in resp:
           dataArray.append(json.loads(x))

        x = []
        y = []
        for i in dataArray:
            y.append(i['pm25'])
            val = i['ts']            
            x.append(datetime.datetime.strptime(val, '%Y-%m-%d %H:%M:%S'))


        plt.title('PMT Data')
        plt.ylabel('Y axis')
        plt.xlabel('X axis')
        plt.plot(x, y, 'b', label='PM 25', linewidth=2)
        #plt.grid(False,color='k')
        plt.show()

    else:
        print("main: Request Failed! status code {}".format(r.status_code))


def getPMTPlotData():
    
    dataArray = []

    now = datetime.datetime.now()
    dt = datetime.datetime.now() - datetime.timedelta(hours = 8)

    r = requests.get("http://192.168.1.74:5000/getPMTPlotByDate", params={'start': dt, 'end': now})

    print("response is: {}\n".format(r))

    if (r.status_code == 200):

        print("getPMTPlotData: request was successful!\n")


    else:
        print("main: Request Failed! status code {}".format(r.status_code))


def main():
    
    #getPMTData()
    getPMTPlotData()

if __name__ == "__main__":
    main()
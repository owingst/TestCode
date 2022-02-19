#!/usr/bin/env python3
""" checkProcs Module """
# -*- coding: utf-8 -*-
# =============================================================================
# Title           : checkProcs.py
# Description     : This script handles process identification
# Created By      : Tim Owings
# Created Date    : Feb 16, 2022
# Python          : 3.9.2
# =============================================================================
import psutil
import subprocess
from subprocess import Popen, PIPE
import json
import utilities
from datetime import datetime


def checkThreads():
    """ checkThreads """

    try:
        mylist = []
        proc = Popen(['pgrep', 'sdrsensor'], stdout=PIPE, stderr=PIPE)
        stdout, _stderr = proc.communicate()
        pid = int(stdout)
        ppid = str(pid)
        output = subprocess.Popen(["ps", "-To", "comm", "-p", ppid,
                                  "--no-headers"], stdout=subprocess.PIPE).stdout.readlines()
        for x in output:

            s = x.decode('ascii').rstrip("\n")
            mylist.append(s)
        return mylist

    except Exception as e:
        print("checkThreads: Exception is {}\n".format(e))


def checkIfProcessRunning(processName):
    """ Check if there is any running process that contains the given name processName. """

    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        # except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
        except Exception as e:
            print("Exception {} for processName: {} processStatus \n".format(e, processName, proc.status()))
            pass
    return False;


if __name__ == "__main__":

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print ("************** checkProcs running at {} ************** \n".format(now))

    tlist = checkThreads()

    if (checkIfProcessRunning("sdrsensor")):

        print("checkThreads: sdrsensor running\n")

        if (checkIfProcessRunning("flaskservice")):

           print("checkThreads: flaskservice running\n")

           if (checkIfProcessRunning("rtl_433")):

              print("checkThreads: rtl_433 running\n")

              if (checkIfProcessRunning("mosquitto")):

                  print("checkThreads: mosquitto running\n") 

                  if ("F007Thread" in tlist):

                     print("checkThreads: F007Thread thread running\n")

                     if ("WeatherThread" in tlist):

                         print("checkThreads: WeatherThread thread running\n")

                         if ("DscThread" in tlist):
                             print("checkThreads: DscThread thread running\n")
                             
                             print("checkThreads: Everything is up and running\n")
                             print ("************** End of checkProcs ************** \n")
   
    else:
        util = utilities.Utility()
        util.pushErrorMsg()

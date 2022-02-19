#!/usr/bin/env python3
""" dumpProcesses Module """
# -*- coding: utf-8 -*-
# =============================================================================
# Title           : dumpProcesses.py
# Description     : This script handles process identification
# Created By      : Tim Owings
# Created Date    : Feb 16, 2022
# Python          : 3.9.2
# =============================================================================
import psutil


def dumpProcs():
    """ Dump processes """
    
    proclist = []

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['name', 'pid', 'status'])
            proclist.append(pinfo)

        except Exception as e:
            print("Exception {} for processName: {} processStatus \n".format(e, proc.name(), proc.status()))
            pass
    return proclist


if __name__ == "__main__":

    procList = dumpProcs()
    for x in procList:
        print(" {}\n".format(x))

#!/usr/bin/env python3
""" TestSMS Module """
# -*- coding: utf-8 -*-
# =============================================================================
# Title           : testsms.py
# Description     : This script sends sms message
# Created By      : Tim Owings
# Created Date    : Jan 17, 2022
# Python          : 3.9.2
# =============================================================================
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import sys


def smssend(emailaddr, app_password, sms_gateway):
    """ Send SMS Message via Gmail SMS """

    server = None

    try:

        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.starttls()

        server.login(emailaddr, app_password)

        msg = MIMEMultipart()

        msg['From'] = emailaddr
        msg['To'] = emailaddr
        msg['Subject'] = "Test SMS Subject"

        msg.attach(MIMEText("Test SMS Body", 'plain'))

        sms = msg.as_string()
    
        server.sendmail(emailaddr, sms_gateway, sms)

        print("smssend: Msg Sent.....\n")

    except Exception as e:
        print("smssend: Exception is {}\n".format(e))

if __name__ == "__main__":
      
    smssend(sys.argv[1],sys.argv[2], sys.argv[3])  
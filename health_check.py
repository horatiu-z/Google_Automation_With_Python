#!/usr/bin/env python3

import psutil
import socket
import emails
import os

def CPU_check():
    """Check if CPU is over 80% usage"""
    if psutil.cpu_percent() > 80 :
        return True
    else: return False

def Disk_check():
    """Check if disk is above 80% used"""
    if psutil.disk_usage('/').percent > 80:
        return True
    else: return False

def Memory_check():
    """Check if left memory is unde 500 MB"""
    if psutil.virtual_memory().available/10**6 < 500:
        return True
    else: return False

def localhost_ip():
    """Check if local host is active"""
    if not socket.gethostbyname(socket.gethostname()) == "127.0.0.1":
        return = True
    else: return False

def main():
    """Automaticaly send an Error email if one of the checks fail - SET TO BE A CRONJOB"""
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    body = "Please check your system and resolve the issue as soon as possible"
    if CPU_check() == True:
        subject = "Error - CPU usage is over 80%"
        message = emails.generate_error_report(sender, receiver, subject, body)
        emails.send(message)
    if Disk_check() == True:
        subject = "Error - Available disk space is less than 20%"
        message = emails.generate_error_report(sender, receiver, subject, body)
        emails.send(message)
    if Memory_check() == True:
        subject = "Error - Available memory is less than 500MB"
        message = emails.generate_error_report(sender, receiver, subject, body)
        emails.send(message)
    if localhost_ip() == True:
        subject = "Error - localhost cannot be resolved to 127.0.0.1"
        message = emails.generate_error_report(sender, receiver, subject, body)
        emails.send(message)

if __name__ == '__main__':
    main()

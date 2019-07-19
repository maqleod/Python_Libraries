#!/usr/bin/env python3

'''
python2/3

This module provides a collection of admin methods

currently only implemented for *nix
'''

from datetime import timedelta
import time
import misc

def uptime():
    '''Gets system uptime

    Args:
        None

    Returns:
        uptime_string (str): output if success, err if failed

    '''
    with open('/proc/uptime') as f:
        uptime_seconds = float(f.readline().split()[0])
        uptime_string = str(timedelta(seconds = uptime_seconds))
        return uptime_string


def processes():
    '''Gets all running processes

    Args:
        None.

    Returns:
        list of processes as tuples

    '''
    cmd = 'ps -auwx'
    status, output, err = misc.run_cmd(cmd)
    if status != 0:
        response = err
    else:
        response = []
        out = output.split("\n")
        del out[0]
        if out[-1] == "":
            del out[-1]
        for line in out:
            response.append(tuple(line.rstrip().split()))
    return response


def users():
    '''Gets all logged on users

    Args:
        None.

    Returns:
        list of logged-on users as tuples

    '''
    cmd = 'who'
    status, output, err = misc.run_cmd(cmd)
    if status != 0:
        response = err
    else:
        response = []
        out = output.split("\n")
        if out[-1] == "":
            del out[-1]
        for line in out:
            response.append(tuple(line.rstrip().split()))
    return response


def current_user():
    '''Gets the currently logged on user

    Args:
        None.

    Returns:
        currently logged-on user as string

    '''
    cmd = 'whoami'
    status, output, err = misc.run_cmd(cmd)
    if status != 0:
        response = err
    else:
        response = output.rstrip()
    return response


def system_time():
    localtime = time.ascitime(time.time())
    return localtime

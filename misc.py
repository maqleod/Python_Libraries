#!/usr/bin/env python3

'''
written by Jared Epstein
'''

import subprocess

def parse_cmd(cmd):
    '''convert a string command into a tuple of arguments

    Args:
        cmd (str): command as string, ex "ls -l"

    Returns:
        cmd_tuple (tuple): tuple of strings for each argument

    '''
    cmd_tuple = tuple(str(cmd).split())
    return cmd_tuple

def run_cmd(cmd):
    '''Wrapper for shell commands

    Args:
        cmd (str): command to run

    Returns:
        response (tuple): return code, output, error

    '''
    p_cmd = parse_cmd(cmd)
    try:
        output = subprocess.Popen(p_cmd, stdout=subprocess.PIPE, shell=False)
        data = output.communicate()
        rc = output.returncode
        err = output.stderr
        response = (rc, data[0].decode('UTF-8'), err)
        return response
    except Exception as e:
        response = (1, "", e)
        return response

def ping_host(host, count = 1, timeout = 1):
    '''Wrapper for ping

    Args:
        host (str): hostname or IP
        count (int): number of times to ping (default 1)
        timeout (int): time to wait for response (default 1)

    Returns:
        response (str): output if success, err if failed

    '''
    cmd = "ping -c " + str(count) + " -W " + str(timeout) + " " +  host
    status, output, err = run_cmd(cmd)
    if status != 0:
        response = err
    else:
        response = output
    return response

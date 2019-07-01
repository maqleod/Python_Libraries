#!/usr/bin/env python3

'''
python2/3

Collection of uncategorized methods.

currently only implemented for *nix
'''

import subprocess

def parse_cmd(cmd):
    '''Convert a string command into a tuple of arguments

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
    # with shell=False, cmd must be a tuple with each arg as its own str
    p_cmd = parse_cmd(cmd)
    try:
        output = subprocess.Popen(p_cmd, stdout=subprocess.PIPE, shell=False)
        data = output.communicate()
        rc = output.returncode
        err = output.stderr
        # this returns as a byte literal, so decode to str
        response = (rc, data[0].decode('UTF-8'), err)
        return response
    except Exception as e:
        # if we hit an error, keep response format the same, provide
        # exception as we would any other error
        response = (1, "", e)
        return response

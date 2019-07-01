#!/usr/bin/env python3

'''
python2/3

This module provides a collection of filesystem
related methods. These build on the file_ex
library to create unix-like fs management.

currently only implemented for *nix
'''

import os
import sys
import re
import file_ex
import misc

def dir_list(dir, depth = 1):
    '''Gets all files in a directory

    Args:
        directory path as string
        depth as int, defaults to 1, 0 = all

    Returns:
        list of files

    '''
    if os.path.exists(dir):
        if os.path.isdir(dir):
            file_list = []
            for root, directories, files in os.walk(dir):
                for filename in files:
                    file_list.append(os.path.join(root,filename))
            return file_list
        else:
            sys.exit(1) #EINVAL path not a directory
    else:
        sys.exit(1) #EIO path not found


def dir_list_ex(dir, depth = 1):
    '''Gets all files and attributes in a directory

    Args:
        directory path as string
        depth as int, defaults to 1, 0 = all

    Returns:
        list of objects containing file attributes

    '''
    if os.path.exists(dir):
        if os.path.isdir(dir):
            file_list = []
            for root, directories, files in os.walk(dir):
                for filename in files:
                    f = file_ex.file_ex(os.path.join(root,filename))
                    file_list.append(f)
            return file_list
        else:
            sys.exit(1) #EINVAL path not a directory
    else:
        sys.exit(1) #EIO path not found


def mounts():
    '''Gets all mounts

    Args:
        None.

    Returns:
        list of mounts as tuples

    '''
    cmd = 'mount -v'
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


def filesystems():
    '''Gets all mounted filesystems

    Args:
        None.

    Returns:
        list of filesystems as tuples

    '''
    cmd = 'df'
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


def disks(): # this returns, but doesn't pull out the characters as it should
    '''Gets all disks and partitions

    Args:
        None.

    Returns:
        list of disks and partitions as tuples

    '''
    cmd = 'lsblk'
    status, output, err = misc.run_cmd(cmd)
    if status != 0:
        response = err
    else:
        response = []
        out = re.sub('[\u251c\u2500\u2514]', '', output).split("\n")
        del out[0]
        if out[-1] == "":
            del out[-1]
        for line in out:
            response.append(tuple(line.rstrip().split()))
    return response

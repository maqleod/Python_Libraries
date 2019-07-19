#!/usr/bin/env python3

'''
python2/3

This module provides a collection of admin methods

currently only implemented for *nix
'''

import os
import string
import re
import misc

def membytes():
    '''Gets mem in bytes and gigabytes

    Args:
        None.

    Returns:
        list of containing both stats as int

    '''
    mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
    mem_gib = mem_bytes/(1024.**3)
    response = (mem_bytes, mem_gib)
    return response

def mem_stats():
    '''Gets mem and swap stats from free

    Args:
        None.

    Returns:
        dictionary of mem stats

    '''
    cmd = 'free'
    status, output, err = misc.run_cmd(cmd)
    if status != 0:
        response = err
    else:
        response = []
        stats = {}
        out = output.split("\n")
        del out[0]
        if out[-1] == "":
            del out[-1]
        # first parse it into an orderly fashion
        for line in out:
            response.append(tuple(line.rstrip().split()))
        # then build the dictionary since the order is known
        stats.update({"total_mem_bytes" : response[0][1]})
        stats.update({"used_mem_bytes" : response[0][2]})
        stats.update({"free_mem_bytes" : response[0][3]})
        stats.update({"shared_mem_bytes" : response[0][4]})
        stats.update({"buffcache_mem_bytes" : response[0][5]})
        stats.update({"avail_mem_bytes" : response[0][6]})
        stats.update({"total_swap_bytes" : response[1][1]})
        stats.update({"used_swap_bytes" : response[1][2]})
        stats.update({"free_swap_bytes" : response[1][3]})
    return stats


def cpu_stats(): # WHY ARE FUNKY CHARACTERS SHOWING UP IN stat_name????
    '''Gets cpu stats

    Args:
        None.

    Returns:
        dictionary of cpu stats

    '''
    cmd = 'top -n1'
    status, output, err = misc.run_cmd(cmd)
    if status != 0:
        response = err
    else:
        response = {}
        stats = {}
        out = output.split("\n")
        for line in out:
            if "%Cpu" in line:
                cpus = line.lstrip().split(":")[1].rstrip()
                for stat in cpus.split(","):
                    stat_name = stat.lstrip().split()[2]
                    stat_value = stat.lstrip().split()[1]
                    response.update({stat_name : stat_value})
    return response

#!/usr/bin/env python3

'''
python2/3

This module provides a collection of networking
related methods.

currently only implemented for *nix
'''

import socket
import misc

##TEST UTILITIES##
def ping_host(host, count = 1, timeout = 1):
    '''Wrapper for ping using run_cmd()

    Args:
        host (str): hostname or IP
        count (int): number of times to ping (default 1)
        timeout (int): time to wait for response (default 1)

    Returns:
        response (str): output if success, err if failed

    '''
    cmd = "ping -c " + str(count) + " -W " + str(timeout) + " " +  host
    status, output, err = misc.run_cmd(cmd)
    if status != 0:
        response = err
    else:
        response = output
    return response


def test_connection(addr, port):
    '''Check to see if a socket can be created

    Args:
        addr (str): ip address of end point
        port (int): port of end point

    Returns:
        is_avail (int): 0 for success, -1 for failure

    '''
    is_avail = 0
    s = socket.socket()
    try:
        s.connect((addr, int(port)))
    except Exception as e:
        is_avail = -1
        return is_avail, e
    finally:
        s.close()
    return is_avail, None


##NETWORK CONFIG##
def get_service_by_port(port, proto):
    '''Gets service bound to specified port

    Args:
        port (int): port number
        proto (str): protocol, either tcp or udp

    Returns:
        service (str): output if success, err if failed

    '''
    try:
        service = socket.getservbyport(port, proto)
        return service
    except socket.error as e:
        return e


def arp():
    '''Gets ARP table

    Args:
        None

    Returns:
        response (list of tuples): output if success, err if failed

    '''
    try:
        with open("/proc/net/arp") as f:
            arp = f.readlines()
            response = []
            for line in arp:
                response.append(tuple(line.rstrip().split()))
            del response[0]
            return response
    except Exception as e:
        return e


def dns():
    '''Gets configured DNS servers

    Args:
        None

    Returns:
        response (list of tuples): output if success, err if failed

    '''
    try:
        with open("/etc/resolv.conf") as f:
            resolv = f.readlines()
            response = []
            for line in resolv:
                if "nameserver" in line:
                    response.append(tuple(line.rstrip().split()))
            return response
    except Exception as e:
        return e


def ifaces():
    '''Gets all interfaces

    Args:
        None

    Returns:
        ifaces (list of dicts): output if success, err if failed
            dict is in format {name: X, flags: X, mtu: X, state: X, mac: X}

    '''
    try:
        ifaces = []
        ip_addr = misc.run_cmd("ip addr")[1]
        lines = ip_addr.split("\n")
        for line in lines:
            if "mtu" in line:
                iface = ['name', line.split(":")[1:2][0].strip()]
                flags = ['flags', line.split()[2]]
                mtu = line.split()[3:5]
                state = line.split()[7:9]
                ifc = iface + flags + mtu + state
                entry = {ifc[i]: ifc[i+1] for i in range(0, len(ifc), 2)}
            if "ether" in line:
                mac = line.split()[1]
                entry.update({'mac': mac})
                ifaces.append(entry)
        return ifaces
    except Exception as e:
        return e


def ips():
    '''Gets configured ips and interfaces

    Args:
        None

    Returns:
        ip_addrs (dict): output if success, err if failed
            dict is in format {ip/prefix: iface}

    '''
    try:
        ifcs = ifaces()
        ip_addrs = {}
        ip_addr = misc.run_cmd("ip addr")[1]
        lines = ip_addr.split("\n")
        for line in lines:
            if "inet" in line:
                cidr = line.split()[1]
                iface = line.split()[-1]
                for ifc in ifcs:
                    if iface == ifc['name']:
                        ip_addrs.update({cidr: iface})
        return ip_addrs
    except Exception as e:
        return e


def routes():
    '''Gets configured routes

    Args:
        None

    Returns:
        entries (list of tuples): output if success, err if failed

    '''
    try:
        entries = []
        out = misc.run_cmd("netstat -rn")
        for line in out[1].rstrip().split("\n"):
            entries.append(tuple(line.split()))
        del entries[0]
        del entries[0]
        return entries
    except Exception as e:
        return e


def hosts():
    '''Gets host file entries
    
    Args:
        None
        
    Returns:
        entries (list of tuples): output if success, err if failed
    '''
    try:
        with open("/etc/hosts") as f:
            hosts = f.readlines()
            response = []
            for line in hosts:
                response.append(tuple(line.rstrip().split()))
            return response
    except Exception as e:
        return e
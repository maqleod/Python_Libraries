#!/usr/bin/env python3

'''
python2/3

this is merely just a shortcut class to make
pulling system info from many different places
a lot easier

currently only implemented for *nix
'''

# built-ins
import socket
import platform
# internal
import core
import net
import fs
import admin

class SysPro():
    def __init__(self):
        # system
        self.hostname = socket.gethostname()
        self.ps = admin.processes()
        self.users = admin.users()
        self.current_user = admin.current_user()
        self.system_time = admin.system_time()
        # hardware
        self.machine = platform.machine()
        self.version = platform.version()
        self.platform = platform.platform()
        self.uname = platform.uname()
        self.system = platform.system()
        self.processor = platform.processor()
        self.mem_stats = core.mem_stats()
        self.cpu_usage = "" # core.cpu_usage()
        # network
        self.ifaces = net.ifaces()
        self.ips = net.ips()
        self.routes = net.routes()
        self.arp = net.arp()
        self.dns = net.dns()
        self.hosts = net.hosts()
        self.sockets = "" # net
        self.net_stats = "" # net
        # filesystem
        self.mounts = fs.mounts()
        self.filesystems = fs.filesystems()
        self.disks = fs.disks()

    def update(self):
        '''Updates volatile system info

        Args:
            None.

        Returns:
            None.

        '''
        self.ps = admin.processes()
        self.users = admin.users()
        self.system_time = admin.system_time()
        self.mem_stats = core.mem_stats()
        self.cpu_usage = "" # core.cpu_usage()
        self.arp = net.arp()
        self.filesystems = fs.filesystems()

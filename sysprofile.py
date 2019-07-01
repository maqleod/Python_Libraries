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
import os
# internal
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
        # hardware
        self.machine = platform.machine()
        self.version = platform.version()
        self.platform = platform.platform()
        self.uname = platform.uname()
        self.system = platform.system()
        self.processor = platform.processor()
        self.mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
        self.mem_gib = self.mem_bytes/(1024.**3)
        # network
        self.ifaces = net.ifaces()
        self.ips = net.ips()
        self.routes = net.routes()
        self.arp = net.arp()
        self.dns = net.dns()
        self.hosts = net.hosts()
        # filesystem
        self.mounts = fs.mounts()
        self.filesystems = fs.filesystems()
        # stats - these need to use @property to update each time they're accessed
        #self.cpu_usage = ""
        #self.mem_usage = ""
        #self.net_throughput = ""
        #self.system_time = ""

    def update(self):
        '''Updates system info

        Args:
            None.

        Returns:
            None.

        '''
        pass
#!/usr/bin/env python

import platform
import commands #this should change to subprocess

'''
This module provides a collection of networking
related methods. These provide reporting and 
management for network resources.

currently only implemented for *nix
'''

def get_routes():
	'''
	gets all routes in route table
	argument: None
	return: tuple of route entries as strings in list format:
		["Dest","Gateway","Mask","Flags","Iface"]
	'''
	route_list = ""
	platform_desc = platform.platform()
	if "Linux" in platform_desc:
		routetable = commands.getoutput('netstat -rn|sed "1,2d"')
		routes = routetable.split('\n')
		new_routes = []
		for route in routes:
			route = route.split()
			del route[6] #del metric
			del route[5] #del ref
			del route[4] #del use
			new_routes.append(route)
		route_list = tuple(new_routes)
	return route_list
	
def get_arp_table():
	'''
	gets all entries in arp table
	argument: None
	return: tuple of arp entries as strings in list format:
		["Addr","MAC","Proto","Iface"]
	'''
	arp_list = ""
	platform_desc = platform.platform()
	if "Linux" in platform_desc:
		arptable = commands.getoutput('arp -an')
		arps = arptable.split('\n')
		new_arps = []
		for arp in arps:
			arp = arp.split()
			arp[1] = arp[1].translate(None,'()')
			arp[4] = arp[4].translate(None,'[]')
			del arp[5] #del on
			del arp[2] #del at
			del arp[0] #del ?
			new_arps.append(arp)
		arp_list = tuple(new_arps)
	return arp_list




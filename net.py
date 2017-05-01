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
		# this should check for route and netstat, default should be route if available
		routetable = commands.getoutput('netstat -rn|sed "1,2d"')
		routes = routetable.split('\n')
		new_routes = []
		#needs option for incomplete
		for route in routes:
			route = route.split()
			del route[6] #del metric
			del route[5] #del ref
			del route[4] #del use
			new_routes.append(route)
		route_list = tuple(new_routes)
	if "BSD" in platform_desc:
		routetable = commands.getoutput('netstat -rn|egrep "/|default"|grep -v lo0')
		routes = routetable.split('\n')
		new_routes = []
		for route in routes:
			route = route.split()
			new_routes.append(route)
		route_list = tuple(new_routes)
	if "Windows" in platform_desc:
		pass
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
	if "BSD" in platform_desc:
		arptable = commands.getoutput('arp -an')
		arps = arptable.split('\n')
		new_arps = []
		for arp in arps:
			if "permanent" in arp:
				arp = arp.split()
				arp[1] = arp[1].translate(None,'()')
				arp[7] = arp[7].translate(None,'[]')
				del arp[6] #del permanent
				del arp[4] #del on
				del arp[2] #del at
				del arp[0] #del ?
				arp = [arp[0],arp[1],arp[3],arp[2]]
				new_arps.append(arp)
			if "expires" in arp:
				arp = arp.split()
				arp[1] = arp[1].translate(None,'()')
				arp[10] = arp[10].translate(None,'[]')
				del arp[9] #del seconds
				del arp[8] #del X
				del arp[7] #del in
				del arp[6] #del expires
				del arp[4] #del on
				del arp[2] #del at
				del arp[0] #del ?
				arp = [arp[0],arp[1],arp[3],arp[2]]
				new_arps.append(arp)
			if "incomplete" in arp:
				arp = arp.split()
				arp[1] = arp[1].translate(None,'()')
				arp[6] = arp[6].translate(None,'[]')
				del arp[4] #del on
				del arp[2] #del at
				del arp[0] #del ?
				arp = [arp[0],arp[1],arp[3],arp[2]]
				new_arps.append(arp)
		arp_list = tuple(new_arps)
	if "Windows" in platform_desc:
		pass
	return arp_list



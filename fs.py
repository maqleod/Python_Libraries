#!/usr/bin/env python

'''
This module provides a collection of filesystem
related methods. These build on the file_ex
library to create unix-like fs management.

currently only implemented for *nix
'''

import os
import sys
import commands
import file_ex

def dir_list(dir, depth = 1):
	'''
	gets all files in a directory
	argument: directory path as string
			  depth as int, defaults to 1, 0 = all
	return: list of files
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
	'''
	gets all files and attributes in a directory
	argument: directory path as string
			  depth as int, defaults to 1, 0 = all
	return: list of objects containing file attributes
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

def get_mounts():
	'''
	gets all mounts
	argument: None
	return: list of mounts as strings
	'''
	mount = commands.getoutput('mount -v')
	mounts = mount.split('\n')
	return mounts
	
def get_filesystems():
	'''
	gets all mounted filesystems
	argument: None
	return: list of filesystems as strings
	'''
	df = commands.getoutput('df|sed "1d"')
	fs = df.split('\n')
	return fs
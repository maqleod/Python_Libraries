#!/usr/bin/env python

'''
This module provides a class that can be built
based off of a file object resulting from an 
open() call or simply a file path as a string

If a file path is given and path does not exists,
all attributes will be None.

These are base calls required for "ls"
currently only implemented for *nix
'''

import os
import datetime
from pwd import getpwuid
from grp import getgrgid

class file_ex:
	def __init__(self,sfile):
		self.ext = self.get_file_ext(sfile)
		self.fullpath = self.get_file_fullpath(sfile)
		self.path = self.get_file_path(sfile)
		self.name = self.get_file_name(sfile)
		self.size = self.get_file_size(sfile)
		self.perms = self.get_file_perms(sfile)
		self.uowner = self.get_file_uowner(sfile)
		self.gowner = self.get_file_gowner(sfile)
		self.mtime = self.get_file_mtime(sfile)
		self.atime = self.get_file_atime(sfile)
		self.ctime = self.get_file_ctime(sfile)
	
	def get_file_ext(self,sfile):
		'''
		gets extension of a file
		argument: file instance or file path as string
		return: extension as string
		'''
		ext = ""
		if isinstance(sfile, file):
			if "." in sfile.name:
				ext = sfile.name.split(".")[-1]
			return ext
		else:
			if os.path.exists(sfile):
				ext = sfile.split(".")[-1]
				return ext
		return None

	def get_file_fullpath(self,sfile):
		'''
		gets path and name of a file
		argument: file instance or file path as string
		return: path as string
		'''
		path = ""
		if isinstance(sfile, file):
			path = os.path.realpath(sfile.name)
			return path
		else:
			if os.path.exists(sfile):
				path = os.path.realpath(sfile)
				return path
		return None

	def get_file_path(self,sfile):
		'''
		gets path of a file
		argument: file instance or file path as string
		return: path as string
		'''
		path = ""
		if isinstance(sfile, file):
			fullpath = os.path.realpath(sfile.name).split("/")
			path = "/".join(fullpath[:-1 or None])
			return path
		else:
			if os.path.exists(sfile):
				fullpath = os.path.realpath(sfile).split("/")
				path = "/".join(fullpath[:-1 or None])
				return path
		return None
		
	def get_file_name(self,sfile):
		'''
		gets name of a file
		argument: file instance or file path as string
		return: name as string
		'''
		name = ""
		if isinstance(sfile, file):
			name = sfile.name.split("/")[-1]
			return name
		else:
			if os.path.exists(sfile):
				name = sfile.split("/")[-1]
				return name
		return None
		
	def get_file_size(self,sfile):
		'''
		gets size of file in bytes
		argument: file instance or file path as string
		return: size in bytes as int
		'''
		size = 0
		if isinstance(sfile, file):
			size = os.path.getsize(self.get_file_fullpath(sfile))
			return size
		else:
			if os.path.exists(sfile):
				size = os.path.getsize(self.get_file_fullpath(sfile))
				return size
		return None

	def get_file_perms(self,sfile):
		'''
		gets permissions mask of a file
		argument: file instance or file path as string
		return: 4 digit mask as int
		'''
		perms = 0
		if isinstance(sfile, file):
			perms = oct(os.stat(self.get_file_fullpath(sfile)).st_mode & 0777)
			return perms
		else:
			if os.path.exists(sfile):
				perms = oct(os.stat(self.get_file_fullpath(sfile)).st_mode & 0777)
				return perms
		return None

	def get_file_uowner(self,sfile):
		'''
		gets user owner of a file
		argument: file instance or file path as string
		return: user that owns file as string
		'''
		user = ""
		if isinstance(sfile, file):
			user = getpwuid(os.stat(self.get_file_fullpath(sfile)).st_uid).pw_name
			return user
		else:
			if os.path.exists(sfile):
				user = getpwuid(os.stat(self.get_file_fullpath(sfile)).st_uid).pw_name
				return user
		return None

	def get_file_gowner(self,sfile):
		'''
		gets group owner of a file
		argument: file instance or file path as string
		return: group that owns file as string
		'''
		group = ""
		if isinstance(sfile, file):
			group = getgrgid(os.stat(self.get_file_fullpath(sfile)).st_gid).gr_name
			return group
		else:
			if os.path.exists(sfile):
				user = getpwuid(os.stat(self.get_file_fullpath(sfile)).st_uid).pw_name
				return user
		return None
		
	def get_file_mtime(self,sfile):
		'''
		gets modified time of a file
		argument: file instance or file path as string
		return: modified time of a file as datetime
		'''
		mtime = ""
		if isinstance(sfile, file):
			mtime = datetime.datetime.fromtimestamp(os.stat(self.get_file_fullpath(sfile)).st_mtime).strftime('%Y-%m-%d %H:%M')
			return mtime
		else:
			if os.path.exists(sfile):
				mtime = datetime.datetime.fromtimestamp(os.stat(self.get_file_fullpath(sfile)).st_mtime).strftime('%Y-%m-%d %H:%M')
				return mtime
		return None

	def get_file_btime(self,sfile):
		'''  unix only
		gets create (birth) time of a file
		argument: file instance or file path as string
		return: create (birth) time of a file as datetime
		'''
		btime = ""
		if isinstance(sfile, file):
			btime = datetime.datetime.fromtimestamp(os.stat(self.get_file_fullpath(sfile)).st_birthtime).strftime('%Y-%m-%d %H:%M')
			return btime
		else:
			if os.path.exists(sfile):
				btime = datetime.datetime.fromtimestamp(os.stat(self.get_file_fullpath(sfile)).st_birthtime).strftime('%Y-%m-%d %H:%M')
				return btime
		return None

	def get_file_atime(self,sfile):
		'''
		gets access time of a file
		argument: file instance or file path as string
		return: access time of a file as datetime
		'''
		atime = ""
		if isinstance(sfile, file):
			atime = datetime.datetime.fromtimestamp(os.stat(self.get_file_fullpath(sfile)).st_atime).strftime('%Y-%m-%d %H:%M')
			return atime
		else:
			if os.path.exists(sfile):
				atime = datetime.datetime.fromtimestamp(os.stat(self.get_file_fullpath(sfile)).st_atime).strftime('%Y-%m-%d %H:%M')
				return atime
		return None

	def get_file_ctime(self,sfile):
		'''
		gets create (birth) time of a file
		argument: file instance or file path as string
		return: create (birth) time of a file as datetime
		'''
		ctime = ""
		if isinstance(sfile, file):
			ctime = datetime.datetime.fromtimestamp(os.stat(self.get_file_fullpath(sfile)).st_ctime).strftime('%Y-%m-%d %H:%M')
			return ctime
		else:
			if os.path.exists(sfile):
				ctime = datetime.datetime.fromtimestamp(os.stat(self.get_file_fullpath(sfile)).st_ctime).strftime('%Y-%m-%d %H:%M')
				return ctime
		return None
			


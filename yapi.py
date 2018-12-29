#YAPI Rewrite - Yet Another Package Manager

#Imports
import configparser
import os
import sys
import installer
import interface

#Config Reading
config = configparser.ConfigParser()
config.read('config.ini')
platform = config['OS']['platform']
cache_boolean =("True" == config['CACHE']['keep_cache'])
cache_location = config['CACHE']['cache_location']
remote_url = config['REMOTE']['location']
remote_branch = config['REMOTE']['location_branch']
file_extension = config['REMOTE']['file_extension']

#Main Program
if len(sys.argv) == 1:
    result = interface.start()
elif len(sys.argv) == 3:
    if sys.argv[1] == 'install':
        output = installer.full_install(sys.argv[2])

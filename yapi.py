#YAPI Rewrite - Yet Another Package Manager

#Imports
import configparser
import os
import sys
import installer

#Config Reading
config = configparser.ConfigParser()
config.read('config.ini')
operatings = config['OS']['platform']
cache_boolean =("True" == config['CACHE']['keep_cache'])
cache_location = config['CACHE']['cache_location']
remote_url = config['REMOTE']['location']
file_extension = config['REMOTE']['file_extension']

if len(sys.argv) == 3:
    if sys.argv[1] == 'install':
        installer.getFile(operatings, sys.argv[2], sys.argv[2], remote_url, file_extension, cache_location)
        installer.runScript(cache_location, sys.argv[2] + file_extension, cache_boolean)

#YAPI Rewrite - Yet Another Package Manager

#Imports
import configparser
import os
import sys
import wget

#Config Reading
config = configparser.ConfigParser()
config.read("config.ini")
operatings = config['OS']['platform']
cache_location = config['CACHE']['cache_location']
remote_url = config['REMOTE']['location']
file_extension = config['REMOTE']['file_extension']

#Function Definitions
def getFile(operating, package, location):
    file_url = remote_url + "/" + operating + "/" + package + file_extension
    os.chdir(cache_location)
    os.remove(package + file_extension)
    wget.download(file_url, package + file_extension)

if len(sys.argv) == 3:
    if sys.argv[1] == "install":
        getFile(operatings, sys.argv[2], sys.argv[2])

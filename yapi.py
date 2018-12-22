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

#Function Definitions
def getFile(operating, package, location):
    file_url = remote_url + "/" + operating + "/" + package + ".sh"
    os.chdir(cache_location)
    wget.download(file_url, package + ".sh")

if len(sys.argv) == 3:
    if sys.argv[1] == "install":
        getFile(operatings, sys.argv[2], sys.argv[2])

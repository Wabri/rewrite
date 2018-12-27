#YAPI Rewrite - Yet Another Package Manager

#Imports
import configparser
import os
import sys
import installer

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
if len(sys.argv) == 3:
    if sys.argv[1] == 'install':
        full_file = sys.argv[2] + file_extension
        file = sys.argv[2]
        file_url = installer.fix_path(
            remote_url + 'packages-' + platform + '/'
            + remote_branch + '/scripts/' + full_file, platform)
        installer.get_file(file_url, cache_location, full_file)
        installer.run_script(cache_location, full_file, cache_boolean)

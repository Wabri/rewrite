#YAPI Rewrite - Yet Another Package Manager

#Imports
import configparser
import os
import sys
import installer
import interface
import configuration

if (len(sys.argv) != 2) & (sys.argv[1] != 'config'):
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
elif len(sys.argv) ==2:
    if sys.argv[1] == 'config':
        configuration.config_update()
elif len(sys.argv) == 3:
    if sys.argv[1] == 'download':
        full_file = sys.argv[2] + file_extension
        file_url = installer.fix_path(
            remote_url + 'packages-' + platform + '/'
            + remote_branch + '/scripts/' + full_file, platform)
        output = installer.get_file(file_url, cache_location, full_file)
    elif sys.argv[1] == 'run':
        full_file = sys.argv[2] + file_extension
        output = installer.run_script(
            cache_location, full_file, cache_boolean, platform)
    elif sys.argv[1] == 'install':
        output = installer.full_install(sys.argv[2])

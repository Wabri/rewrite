#YAPI Rewrite - Yet Another Package Manager

#Imports
import configparser
import os
import sys
import installer
import interface
import configuration
import search

if len(sys.argv) != 2:
    if (sys.argv[1] == 'config'):
        try:
            #Config Reading
            config = configparser.ConfigParser()
            config.read('config.ini')
            platform = config['OS']['platform']
            cache_boolean = ("True" == config['Cache']['keep_cache'])
            cache_location = config['Cache']['cache_location']
            remote_url = config['Remote']['location']
            remote_branch = config['Remote']['location_branch']
            file_extension = config['Remote']['file_extension']
            search_local = ("True" == config['Search']['search_local'])
            remote_search_dir = config['Search']['packages_search_remote']
        except:
            pass

#Main Program
if len(sys.argv) == 1:
    result = interface.start()
elif len(sys.argv) ==2:
    if sys.argv[1] == 'config':
        configuration.config_update()
elif len(sys.argv) == 3:
    if sys.argv[1] == 'search':
        print(remote_search_dir)
        remote_url = remote_url + 'packages-' + platform + '/' + remote_branch
        pattern = sys.argv[2]
        matches = search.search(pattern, remote_url, file_extension,
            search_local, cache_location)
        for match in matches:
            print(match)
    elif sys.argv[1] == 'download':
        full_file = sys.argv[2] + file_extension
        file_url = remote_url + 'packages-' + platform + '/' + remote_branch + '/scripts/' + full_file
        output = installer.get_file(file_url, cache_location, full_file)
    elif sys.argv[1] == 'run':
        full_file = sys.argv[2] + file_extension
        output = installer.run_script(
            cache_location, full_file, cache_boolean, platform)
    elif sys.argv[1] == 'install':
        output = installer.full_install(sys.argv[2])

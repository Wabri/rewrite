#YAPI Rewrite - Yet Another Package Manager

#Imports
import modules.config_import as config_import
import modules.installer as installer
import gui.interface as interface
import modules.search as search
import json
import sys
import os
try:
    os.chdir(os.path.dirname(__file__)) #Change file location if outside of YAPI
except:
    pass #Already in directory of YAPI.
if len(sys.argv) != 2:
    try:
        config = json.loads(config_import.get_config())
        os_platform = config['OS.platform']
        cache_boolean = ('True' == config['Cache.keep_cache'])
        cache_location = config['Cache.cache_location']
        search_local = ('True' == config['Search.search_local'])
        search_url = config['Search.search_url']
        remote_location = config['Remote.location']
        remote_branch = config['Remote.branch']
        file_extension = config['Remote.file_extension']
    except:
        print('Config not able to be imported. Run \"python3 yapi.py config\" to fix the error')

#Main Program
if len(sys.argv) == 1:
    result = interface.start()
elif len(sys.argv) == 2:
    if sys.argv[1] == 'config':
        config_import.update_config()
elif len(sys.argv) == 3:
    if sys.argv[1] == 'search':
        matches = search.search(search_url, file_extension, search_local, cache_location, sys.argv[2])
        for match in matches:
            print(match)
    elif sys.argv[1] == 'download':
        file_name = sys.argv[2] + file_extension
        file_url = remote_location + os_platform + '/' + remote_branch + '/scripts/' + file_name
        os.chdir(cache_location)
        output = installer.get_file(file_url, file_name)
    elif sys.argv[1] == 'run':
        file_name = sys.argv[2] + file_extension
        os.chdir(cache_location)
        output = installer.run_script(file_name, cache_boolean)
    elif sys.argv[1] == 'install':
        output = installer.full_install(sys.argv[2])

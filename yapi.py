#YAPI Rewrite - Yet Another Package Installer

#Imports
import modules.cross_platform as cp
import modules.config_import as ci
import modules.new_installer as ni
import gui.interface as interface
import json
import sys
import os
try:
    os.chdir(os.path.dirname(__file__)) #Change file location if outside of YAPI
except:
    pass #Already in directory of YAPI.
if len(sys.argv) != 2:
    try:
        config = json.loads(ci.get_config())
        os_platform = config['OS.platform']
        cache_boolean = ('True' == config['Cache.keep_cache'])
        cache_location = config['Cache.cache_location']
        search_local = ('True' == config['Search.search_local'])
        search_url = config['Search.search_url']
        remote_location = config['Remote.location']
        remote_branch = config['Remote.branch']
        file_extension = config['Remote.file_extension']
        language_selected = config['Languages.selected']
    except:
        print('Config not able to be imported. Run \'python3 yapi.py config\' to fix the error')

#Main Program
if len(sys.argv) == 1:
    result = interface.start()

elif len(sys.argv) == 2:
    if sys.argv[1] == 'config':
        ci.update_config()

elif len(sys.argv) == 3:
    if sys.argv[1] == 'search':
        cp.tabprint(ni.search(sys.argv[2], config))
    elif sys.argv[1] == 'type':
        cp.tabprint(ni.type(sys.argv[2], config))
    elif sys.argv[1] == 'download':
        ni.download(sys.argv[2], config)
    elif sys.argv[1] == 'run':
        ni.install(sys.argv[2], config)
    elif sys.argv[1] == 'install':
        ni.download(sys.argv[2], config)
        ni.install(sys.argv[2], config)
    elif sys.argv[1] == 'uninstall':
        ni.uninstall(sys.argv[2], config)

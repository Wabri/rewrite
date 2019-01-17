def get_config():
    #Imports
    import os
    import configparser
    import json

    #Get Config
    conf = {}
    os.chdir('config')
    config = configparser.ConfigParser()
    config.read('config.ini')
    conf['OS.platform']           = config['OS']['platform']
    conf['Cache.keep_cache']      = ("True" == config['Cache']['keep_cache'])
    conf['Cache.cache_location']  = config['Cache']['cache_location']
    conf['Search.search_local']   = ("True" == config['Search']['search_local'])
    conf['Search.search_url']     = config['Search']['search_url']
    conf['Remote.location']       = config['Remote']['location']
    conf['Remote.branch']         = config['Remote']['branch']
    conf['Remote.file_extension'] = config['Remote']['file_extension']
    os.chdir('..')
    return json.dumps(conf)

def update_config():
    #Imports
    import os
    import json
    import platform
    import configparser

    os.chdir('config')
    if os.path.isfile('config.ini') == False:
        import shutil
        shutil.copy('default.ini', 'config.ini')

    config = configparser.ConfigParser()
    config.read('config.ini')

    if platform.system() == 'Linux':
        system = 'linux-' #Include dash for distro that is appended to this string
    elif platform.system() == 'Darwin':
        system = 'darwin'
    elif platform.system() == 'Windows':
        system = 'windows'

    if system == 'linux-':
        import distro
        switch = {
            'debian': 'debian',
            'ubuntu': 'debian'
        }
        system += switch.get(distro.id(), 'error')

    search_base = config['Remote']['search_base']
    search_end = config['Remote']['search_end']
    branch = config['Remote']['location_branch']
    full_search_url = search_base + 'packages-' + system + search_end + branch

    config.set('Search', 'packages_search_remote', full_search_url)
    config.set('OS', 'platform', system)
    cfgfile = open("config.ini",'w')
    config.write(cfgfile)

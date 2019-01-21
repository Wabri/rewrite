def get_config():
    #Imports
    import os
    from configparser import ConfigParser
    from configparser import ExtendedInterpolation
    import json

    #Get Config
    conf = {}
    os.chdir('config')
    config = ConfigParser(interpolation=ExtendedInterpolation())
    config.read('config.ini')
    conf['OS.platform']           = config['OS']['platform']
    conf['Cache.keep_cache']      = config['Cache']['keep_cache']
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
    from configparser import ConfigParser
    from configparser import ExtendedInterpolation

    os.chdir('config')
    #Make config if not present
    if os.path.isfile('config.ini') == False:
        import shutil
        shutil.copy('default.ini', 'config.ini')

    config = ConfigParser(interpolation=ExtendedInterpolation())
    config.read('config.ini')

    if platform.system() == 'Linux':
        system = 'linux-' #Include dash for distro that is appended to this string
        import distro
        switch = {
            'debian': 'debian',
            'ubuntu': 'debian'
        }
        system += switch.get(distro.id(), 'error')
    elif platform.system() == 'Darwin':
        system = 'darwin'
    elif platform.system() == 'Windows':
        system = 'windows'

    config.set('OS', 'platform', system)
    cfgfile = open("config.ini",'w')
    config.write(cfgfile)

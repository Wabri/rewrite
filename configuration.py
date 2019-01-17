def config_update():
    import configparser
    import platform
    import os
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

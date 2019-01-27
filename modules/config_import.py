def get_language(language, platform):
    #Imports
    import os
    from configparser import ConfigParser
    from configparser import ExtendedInterpolation
    import json
    print(os.getcwd())
    #Get Config
    conf = {}
    os.chdir('config/languages')
    config = ConfigParser(interpolation=ExtendedInterpolation())
    config.read(language + '_return.ini')
    if platform == 'windows': #Windows
        dos_return = 'Return_Dos'
        for key in conf.keys():
            conf[key] = config[dos_return][key]
        conf['err_1'] = config['Return_Dos']['err_1']
        conf['err_2'] = config['Return_Dos']['err_2']
        conf['err_3'] = config['Return_Dos']['err_3']
        conf['err_5'] = config['Return_Dos']['err_5']
        conf['err_8'] = config['Return_Dos']['err_8']
        conf['err_12'] = config['Return_Dos']['err_12']
        conf['err_14'] = config['Return_Dos']['err_14']
        conf['err_19'] = config['Return_Dos']['err_19']
        conf['err_54'] = config['Return_Dos']['err_54']
        conf['err_65'] = config['Return_Dos']['err_65']
        conf['err_82'] = config['Return_Dos']['err_82']
        conf['err_148'] = config['Return_Dos']['err_148']
        conf['err_266'] = config['Return_Dos']['err_266']
    else: #Linux or MacOS
        conf['err_0'] = config['Return_Unix']['err_0']
        conf['err_1'] = config['Return_Unix']['err_1']
        conf['err_2'] = config['Return_Unix']['err_2']
        conf['err_11'] = config['Return_Unix']['err_11']
        conf['err_13'] = config['Return_Unix']['err_13']
        conf['err_126'] = config['Return_Unix']['err_126']
        conf['err_127'] = config['Return_Unix']['err_127']
        conf['err_128'] = config['Return_Unix']['err_128']
        conf['err_130'] = config['Return_Unix']['err_130']
    os.chdir('..')
    return json.dumps(conf)

def get_config():
    #Imports
    import os
    from configparser import ConfigParser
    from configparser import ExtendedInterpolation
    import json
    print(os.getcwd())
    #Get Config
    conf = {}
    if os.path.basename(os.getcwd()) != 'config':
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
    conf['Languages.selected']    = config['Languages']['selected']
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

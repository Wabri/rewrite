def get_config():
    #Imports
    import os
    import configparser
    import json

    #Get Config
    conf = {}
    os.chdir('config/')
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

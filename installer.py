def full_install(package):
    import os
    import sys
    import json
    import installer
    import modules.config_import as config_import

    config = json.loads(config_import.get_config())
    os_platform = config['OS.platform']
    cache_boolean = ('True' == config['Cache.keep_cache'])
    cache_location = config['Cache.cache_location']
    search_local = ('True' == config['Search.search_local'])
    search_url = config['Search.search_url']
    remote_location = config['Remote.location']
    remote_branch = config['Remote.branch']
    file_extension = config['Remote.file_extension']

    file_name = package + file_extension
    file_url = remote_location + os_platform + '/' + remote_branch + '/scripts/' + file_name
    get_file(file_url, file_name)
    return run_script(file_name, cache_boolean)

def get_file(file_url, local_name):
    from urllib import request
    import shutil
    import os
    with request.urlopen(file_url) as response, open(local_name, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)

def run_script(file, cache):
    import subprocess
    import os
    try:
        with open(file, 'r') as file_script:
            bashCommand = ''
            for line in file_script.readlines():
                if line[0] != '#':
                    bashCommand += line
            bashCommand = bashCommand.replace('\n', '; ')
            output =subprocess.call(
                bashCommand, stderr=subprocess.STDOUT, shell=True)
            if cache != True:
                os.remove(file)
            return output
    except (OSError, IOError, KeyError):
        return 'Issue Installing'
        if cache != True:
            os.remove(file)

def fix_path(path, platform):
    if platform == "windows":
        path.replace("/", "\\")
    else:
        path.replace("\\", "/")
    return path

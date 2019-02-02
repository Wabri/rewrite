def full_install(package):
    import json
    import modules.config_import as config_import
    import modules.cross_platform as cp

    config = json.loads(config_import.get_config())
    os_platform = config['OS.platform']
    cache_boolean = config['Cache.keep_cache']
    cache_location = config['Cache.cache_location']
    remote_location = config['Remote.location']
    remote_branch = config['Remote.branch']
    file_extension = config['Remote.file_extension']

    file_name = package + file_extension
    file_url = remote_location + os_platform + '/' + remote_branch + '/scripts/' + file_name
    cp.chdir(cache_location, os_platform)
    get_file(file_url, file_name)
    return run_script(file_name, cache_boolean)

def get_file(file_url, file_name):
    from urllib import request
    import shutil
    with request.urlopen(file_url) as response, open(
        file_name, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)

def run_script(file_name, cache_keep):
    import subprocess
    import os
    try:
        with open(file_name, 'r') as file_script:
            bashCommand = ''
            for line in file_script.readlines():
                if line[0] != '#':
                    bashCommand += line
            bashCommand = bashCommand.replace('\n', '; ')
            output = subprocess.call(
                bashCommand, stderr=subprocess.STDOUT, shell=True)
            if cache_keep != 'True':
                os.remove(file_name)
            return output
    except (OSError, IOError, KeyError):
        return 'Issue Installing'
        if cache_keep != 'True':
            os.remove(file_name)

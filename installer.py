def full_install(package):
    import configparser
    import os
    import sys
    import installer

    config = configparser.ConfigParser()
    config.read('config.ini')
    platform = config['OS']['platform']
    cache_boolean =("True" == config['CACHE']['keep_cache'])
    cache_location = config['CACHE']['cache_location']
    remote_url = config['REMOTE']['location']
    remote_branch = config['REMOTE']['location_branch']
    file_extension = config['REMOTE']['file_extension']

    full_file = package + file_extension
    file_url = fix_path(
        remote_url + 'packages-' + platform + '/'
        + remote_branch + '/scripts/' + full_file, platform)
    get_file(file_url, cache_location, full_file)
    return run_script(cache_location, full_file, cache_boolean, platform)

def get_file(file_url, cache_location, local_name):
    from urllib import request
    import shutil
    import os
    os.chdir(cache_location)
    with request.urlopen(file_url) as response, open(local_name, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)

def run_script(directory, file, cache, platform):
    import subprocess
    import os
    try:
        directory = fix_path(os.path.dirname(__file__) + '/'  + directory, platform)
        os.chdir(directory)
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

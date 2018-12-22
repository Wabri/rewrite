def getFile(operating, package, location, remote_url, file_extension, cache_location):
    import wget
    import os
    file_url = remote_url + '/' + operating + '/' + package + file_extension
    os.chdir(cache_location)
    if os.path.isfile(package + file_extension) == False:
        wget.download(file_url, package + file_extension)
        print() #Newline after wget

def runScript(directory, file, cache):
    import subprocess
    import os
    try:
        directory = os.path.dirname(__file__) + '/'  + directory
        os.chdir(directory)
        with open(file, 'r') as file_script:
            bashCommand = ''
            for line in file_script.readlines():
                if line[0] != '#':
                    bashCommand += line
            bashCommand = bashCommand.replace('\n', '; ')
            subprocess.call(
                bashCommand, stderr=subprocess.STDOUT, shell=True)
            if cache != True:
                os.remove(file)
    except (OSError, IOError, KeyError):
        print('Issue Installing')
        if cache != True:
            os.remove(file)

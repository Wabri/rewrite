def getFile(file_url, cache_location, local_name):
    import wget
    import os
    os.chdir(cache_location)
    if os.path.isfile(local_name) == False:
        print(file_url)
        wget.download(file_url, local_name)
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

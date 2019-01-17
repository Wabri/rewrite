def search(pattern, extension, local_boolean, local_dir):
    from urllib import request
    import configparser
    import shutil
    import json
    import os
    import re

    #Read config.ini
    config = configparser.ConfigParser()
    config.read('config.ini')
    api_url = config['Search']['packages_search_remote']
    files = []

    #Get search.json
    with request.urlopen(api_url) as response, open('search.json', 'wb') as out_file:
        shutil.copyfileobj(response, out_file)

    #Parse search.json
    with open('search.json', "r") as search_file:
        data = json.load(search_file)
        for file in data:
            name = file['name']
            if name.endswith(extension):
                files.append(name.replace('.sh', ''))

    #Get local files
    if local_boolean:
        for file in os.listdir(local_dir):
            if file.endswith(extension):
                if file.replace('.sh', '') not in files:
                    files.append(file.replace('.sh', ''))
    #Search
    r = re.compile(pattern)
    result = list(filter(r.match, files))
    return result

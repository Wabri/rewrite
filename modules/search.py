def search(api_url, file_extension, local_boolean, local_dir, search_pattern):
    from urllib import request
    import shutil
    import json
    import os
    import re

    files = []

    #Get search.json
    with request.urlopen(api_url) as api_result, open('search.json', 'wb') as search_file:
        shutil.copyfileobj(api_result, search_file)

    #Parse search.json
    with open('search.json', 'r') as search_file:
        data = json.load(search_file)
        for file in data:
            name = file['name']
            if name.endswith(file_extension):
                files.append(name.replace(file_extension, ''))

    #Get local files
    if local_boolean:
        for file in os.listdir(local_dir):
            if file.endswith(file_extension):
                if file.replace(file_extension, '') not in files:
                    files.append(file.replace('.sh', ''))
    #Search
    r = re.compile(search_pattern)
    result = list(filter(r.match, files))
    return result

def searchType(os_platform, api_url, base_url, branch, file_extension, local_boolean, local_dir, package_type):
    from urllib import request
    info = []
    package_list = search(api_url, file_extension, local_boolean, local_dir, '[\\w+]')
    for package in package_list:
        url = base_url + os_platform + '/' + branch + '/' + local_dir + package + file_extension
        with request.urlopen(url) as response:
            literal_content = response.read()
            unicode_content = literal_content.decode('unicode_escape')
            for line in unicode_content.splitlines():
                if line[0] == '#':
                    info.append(line.replace('# ', ''))
    print(info)
    print()

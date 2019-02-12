def fix_path(path, platform):
    if platform == 'windows':
        path.replace('/', '\\')
    else:
        path.replace('\\', '/')
    return path

def chdir(directory, platform):
    import os
    if os.path.basename(os.getcwd()) != directory:
        os.chdir(fix_path(directory, platform))

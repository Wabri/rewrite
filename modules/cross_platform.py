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

def tabprint(array):
    result = ''
    length = 0
    pos = 0
    # Get length of longest string + 5
    for item in array:
        if len(item) > length:
            length = len(item) + 5
    # Add items to string to print
    for item in array:
        spacer = ''
        for i in range(length - len(item)):
            spacer += ' '
        pos += len(item) + len(spacer)
        if pos <= term_width() - length:
            result += item + spacer
        else:
            pos = 0
            result += '\n'
    print(result)

def term_width():
    import os
    rows, columns = os.popen('stty size', 'r').read().split()
    return int(columns)

def term_height():
    import os
    rows, columns = os.popen('stty size', 'r').read().split()
    return int(rows)

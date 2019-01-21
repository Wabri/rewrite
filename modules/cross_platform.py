def fix_path(path, platform):
    if platform == "windows":
        path.replace("/", "\\")
    else:
        path.replace("\\", "/")
    return path

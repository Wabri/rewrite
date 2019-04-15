def download(package, config):
    # Imports
    from configparser import ConfigParser
    from configparser import ExtendedInterpolation
    import modules.cross_platform as cp
    from urllib import request
    import subprocess
    import shutil

    # Config
    os_platform = config['OS.platform']
    remote_location = config['Remote.location']
    remote_branch = config['Remote.branch']
    file_extension = config['Remote.file_extension']

    # Downloading
    print('--> Downloading Package File')
    file_name = package + file_extension
    file_url = remote_location + os_platform + '/' + remote_branch + '/new-scripts/' + file_name
    cp.chdir('scripts/', os_platform)
    with request.urlopen(file_url) as response, open(
        file_name, 'wb') as  package_file:
            shutil.copyfileobj(response, package_file)

    # Additional Resources
    print('--> Downloading Additional Resources')
    package_file = ConfigParser(interpolation=ExtendedInterpolation())
    package_file.read(file_name)
    package_download = package_file['Script']['download']
    with open(package + '.log', 'a') as package_log:
        subprocess.call(package_download.split(), stdout=package_log)
    cp.chdir('..', os_platform)

def install(package, config):
    # Imports
    from configparser import ConfigParser
    from configparser import ExtendedInterpolation
    import modules.cross_platform as cp
    import subprocess

    # Config
    os_platform = config['OS.platform']
    cp.chdir('scripts/', os_platform)
    file_name = package + config['Remote.file_extension']
    package_file = ConfigParser(interpolation=ExtendedInterpolation())
    package_file.read(file_name)
    package_before = package_file['Script']['before_install']
    package_script = package_file['Script']['install']
    package_after = package_file['Script']['after_install']
    package_desktop = package_file['Script']['desktop_entry']
    print('--> Before Install Script')
    with open(package + '.log', 'a') as package_log:
        subprocess.call(package_before.split(), stdout=package_log)
    print('--> Install Script')
    with open(package + '.log', 'a') as package_log:
        subprocess.call(package_script.split(), stdout=package_log)
    print('--> After Install Script')
    with open(package + '.log', 'a') as package_log:
        subprocess.call(package_after.split(), stdout=package_log)
    print('--> Creating Desktop Entry')
    with open(package + '.log', 'a') as package_log:
        subprocess.call(package_desktop.split(), stdout=package_log)
    cp.chdir('..', os_platform)

def uninstall(package, config):
    # Imports
    from configparser import ConfigParser
    from configparser import ExtendedInterpolation
    import modules.cross_platform as cp
    import subprocess

    # Config
    os_platform = config['OS.platform']
    cp.chdir('scripts/', os_platform)
    file_name = package + config['Remote.file_extension']
    package_file = ConfigParser(interpolation=ExtendedInterpolation())
    package_file.read(file_name)
    package_uninstall = package_file['Script']['uninstall']
    print('--> Uninstall Script')
    with open(package + '.log', 'a') as package_log:
        subprocess.call(package_uninstall.split(), stdout=package_log)
    cp.chdir('..', os_platform)

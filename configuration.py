#Imports
import configparser
import platform
import os

#Config Updating
if os.path.isfile('config.ini') == False:
    import shutil
    shutil.copy('default.ini', 'config.ini')

config = configparser.ConfigParser()
config.read('config.ini')

if platform.system() == 'Linux':
    system = 'linux-' #Include dash for distro that is appended to this string
elif platform.system() == 'Darwin':
    system = 'darwin'
elif platform.system() == 'Windows':
    system = 'windows'

if system == 'linux-':
    import distro
    switch = {
        'debian': 'debian',
        'ubuntu': 'debian'
    }
    system += switch.get(distro.id(), 'error')

config.set('OS', 'platform', system)
cfgfile = open("config.ini",'w')
config.write(cfgfile)

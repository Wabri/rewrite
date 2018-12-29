try:
    import installer
    import toga
    from toga.style.pack import *
except ImportError:
    pass

def build(app):
    def installHandle(widget):
        import installer
        installer.full_install(package)
        # full_file = packageInput.value + yapi.file_extension
        # file = packageInput.value
        # file_url = installer.fix_path(yapi.remote_url + 'packages-' +
        #     yapi.platform + '/' + yapi.remote_branch + '/scripts/' +
        #     full_file, yapi.platform)
        # installer.get_file(file_url, yapi.cache_location, full_file)
        # resultInput.value = installer.run_script(yapi.cache_location,
        #     full_file, yapi.cache_boolean)

    box = toga.Box()
    packageBox = toga.Box()
    packageLabel = toga.Label('Package To Install:')
    packageInput = toga.TextInput()
    submitBox = toga.Box()
    install = toga.Button('Install Package', on_press=installHandle)
    resultBox = toga.Box()
    resultInput = toga.TextInput(readonly = True)

    packageBox.add(packageLabel)
    packageBox.add(packageInput)
    submitBox.add(install)
    resultBox.add(resultInput)
    box.add(listBox)
    box.add(packageBox)
    box.add(submitBox)
    box.add(resultBox)

    box.style.update(direction=COLUMN, padding_top=10)
    listBox.style.update(direction=ROW, padding=5)
    packageBox.style.update(direction=ROW, padding=5)
    submitBox.style.update(direction=ROW, padding=5)
    return box

def start():
    return toga.App('Yet Another Package Installer',
                    'org.YAPI.rewrite', startup=build).main_loop()

def main():
    start().main_loop()

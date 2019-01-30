try:
    import modules.config_import as config_import
    import modules.installer as installer
    import json
    import toga
    import os
    from toga.style.pack import *
except ImportError:
    pass

def build(app):
    #Get Config and Language
    config = json.loads(config_import.get_config())
    os_platform = config['OS.platform']
    language_selected = config['Languages.selected']
    language = json.loads(config_import.get_language(language_selected, os_platform))
    #Button Handles
    def install_handle(widget):
        import modules.installer as installer
        return_code = installer.full_install(packageInput.value)
        resultInput.value = language['err_' + str(return_code)]
    #Create GUI Elements
    box = toga.Box()
    packageBox = toga.Box()
    packageLabel = toga.Label('Package To Install:')
    packageInput = toga.TextInput()
    submitBox = toga.Box()
    install = toga.Button('Install Package', on_press=install_handle)
    resultBox = toga.Box()
    resultInput = toga.TextInput(readonly = True)
    #Nest GUI Elements
    packageBox.add(packageLabel)
    packageBox.add(packageInput)
    submitBox.add(install)
    resultBox.add(resultInput)
    box.add(packageBox)
    box.add(submitBox)
    box.add(resultBox)

    box.style.update(direction=COLUMN, padding_top=10)
    packageBox.style.update(direction=ROW, padding=5)
    submitBox.style.update(direction=ROW, padding=5)
    return box

def start():
    try:
        import toga
    except ImportError:
        pass
    return toga.App('Yet Another Package Installer',
                    'org.YAPI.rewrite', startup=build).main_loop()

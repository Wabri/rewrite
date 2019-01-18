try:
    import modules.installer as installer
    import toga
    from toga.style.pack import *
except ImportError:
    pass

def build(app):
    def installHandle(widget):
        import modules.installer as installer
        resultInput.value = installer.full_install(packageInput.value)
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

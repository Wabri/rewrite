try:
    import modules.config_import as config_import
    import modules.installer as installer
    import modules.search as search
    import json
    import toga
    import os
    from toga.style.pack import *
except ImportError:
    pass

def build(app):
    # Get Config and Language
    config = json.loads(config_import.get_config())
    os_platform = config['OS.platform']
    search_url = config['Search.search_url']
    file_extension = config['Remote.file_extension']
    search_local = ('True' == config['Search.search_local'])
    cache_location = config['Cache.cache_location']
    language_selected = config['Languages.selected']
    language = json.loads(config_import.get_language(language_selected, os_platform))

    # Button Handles
    def install_handle(widget):
        import modules.installer as installer
        return_code = installer.full_install(package_input.value)
        package_install_result.value = language['err_' + str(return_code)]

    def search_handle(widget):
        import modules.search as search
        pattern = search_input.value
        matches = search.search(search_url, file_extension, search_local, cache_location, pattern)
        for match in matches:
            search_result.data.insert(0, match)

    # Main Boxes
    main_box = toga.Box()
    package_box = toga.Box()
    package_input_box = toga.Box()
    package_submit_box = toga.Box()
    search_box = toga.Box()
    search_input_box = toga.Box()
    search_results_box = toga.Box()

    # Package Install
    package_label = toga.Label('Package to Install:')
    package_input = toga.TextInput()
    package_input_box.add(package_label)
    package_input_box.add(package_input)

    package_submit = toga.Button('Install Package', on_press = install_handle)
    package_install_result = toga.TextInput(readonly = True)
    package_submit_box.add(package_submit)
    package_submit_box.add(package_install_result)

    package_box.add(package_input_box)
    package_box.add(package_submit_box)

    # Search Function
    data = []
    search_label = toga.Label('Search Pattern:')
    search_input = toga.TextInput()
    search_button = toga.Button('Search Pattern', on_press = search_handle)
    search_result = toga.Table(headings=['Package'], data=[])
    search_input_box.add(search_label)
    search_input_box.add(search_input)
    search_results_box.add(search_button)
    search_results_box.add(search_result)

    search_box.add(search_input_box)
    search_box.add(search_results_box)

    # Main Box
    main_box.add(package_box)
    main_box.add(search_box)

    # Style Changes
    main_box.style.update(direction=ROW, padding_top=10)
    package_box.style.update(direction=COLUMN, padding_top=10)
    search_box.style.update(direction=COLUMN, padding_top=10)
    package_input_box.style.update(direction=ROW, padding=5)
    search_input_box.style.update(direction=ROW, padding=5)
    search_results_box.style.update(direction=COLUMN, padding=5)

    # Return GUI
    return main_box

def start():
    try:
        import toga
    except ImportError:
        pass
    return toga.App('Yet Another Package Installer',
                    'org.YAPI.rewrite', startup=build).main_loop()

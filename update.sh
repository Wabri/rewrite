#!/bin/bash
cd ~
mv YAPI oldYAPI
cd oldYAPI
sudo rm -r __pycache__
sudo rm -r config
sudo rm -r gui
sudo rm -r modules
sudo rm requirements.txt
sudo rm yapi.py
git clone https://github.com/YetAnotherPackageInstaller/rewrite YAPI
mv YAPI ..

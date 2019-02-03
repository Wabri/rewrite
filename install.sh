#!/bin/bash
cd ~
git clone https://github.com/YetAnotherPackageInstaller/rewrite.git YAPI --depth 1
git clone https://github.com/pybee/toga.git
cd toga
pip3 install -e src/core
pip3 install -e src/dummy
if [[ "$OSTYPE" == "linux-gnu" ]]; then
  pip3 install -e src/gtk
elif [[ "$OSTYPE" == "darwin"* ]]; then
  pip3 install -e src/cocoa
fi
cd ..
cd YAPI
pip3 install -r requirements.txt
sudo rm -r .git* .travis.yml .circleci install.sh LICENSE README.md
ln ~/YAPI/yapi.sh /usr/bin/yapi
python3 yapi.py config
cd ..

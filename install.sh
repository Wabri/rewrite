cd ~
git clone https://github.com/YetAnotherPackageInstaller/rewrite.git --depth 1
git clone https://github.com/pybee/toga.git
cd toga
pip install -e src/core
pip install -e src/dummy
pip install -e src/gtk
cd ..
sudo rm -r toga
cd YAPI
sudo rm -r .git* .travis.yml install.sh .circleci

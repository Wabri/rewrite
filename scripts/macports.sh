#Install macports from source on github - https://www.macports.org/index.php
mkdir -p /opt/mports
cd /opt/mports
git clone https://github.com/macports/macports-base.git
cd /opt/mports/macports-base
./configure --enable-readline
make
sudo make install
make distclean
cd /opt/mports
git clone https://github.com/macports/macports-ports.git

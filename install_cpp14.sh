#/bin/bash
add-apt-repository ppa:ubuntu-toolchain-r/test &&
apt update &&
apt-get -y install build-essential gcc-7 g++-7 &&
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 60 &&
update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-7 60 


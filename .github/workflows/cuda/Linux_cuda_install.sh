#! /bin/bash

if [[ $CUDA_VERSION == "cu102" ]]; then
  distro=ubuntu1804
  sudo apt install --no-install-recommends gcc-8 g++-8
  sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 80 --slave /usr/bin/g++ g++ /usr/bin/g++-8 --slave /usr/bin/gcov gcov /usr/bin/gcov-8
else if [[ $CUDA_VERSION == "cu110" ]]; then
  distro=ubuntu2004
  sudo apt install --no-install-recommends gcc-9 g++-9
  sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 90 --slave /usr/bin/g++ g++ /usr/bin/g++-9 --slave /usr/bin/gcov gcov /usr/bin/gcov-9
else if [[ $CUDA_VERSION == @(cu111|cu112|cu113) ]]; then
  distro=ubuntu2004
  sudo apt install --no-install-recommends gcc-10 g++-10
  sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-10 100 --slave /usr/bin/g++ g++ /usr/bin/g++-10 --slave /usr/bin/gcov gcov /usr/bin/gcov-10
else if [[ $CUDA_VERSION == @(cu114|cu115|cu116) ]]; then
  distro=ubuntu2004
  sudo apt install --no-install-recommends gcc-11 g++-11
  sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-11 110 --slave /usr/bin/g++ g++ /usr/bin/g++-11 --slave /usr/bin/gcov gcov /usr/bin/gcov-11
else if [[ $CUDA_VERSION == @(cu117|cu118) ]]; then
  distro=ubuntu2204
  sudo apt install --no-install-recommends gcc-11 g++-11
  sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-11 110 --slave /usr/bin/g++ g++ /usr/bin/g++-11 --slave /usr/bin/gcov gcov /usr/bin/gcov-11
else if [[ $CUDA_VERSION == @(cu120|cu121|cu122|cu123) ]]; then
  distro=ubuntu2204
  sudo apt install --no-install-recommends gcc-12 g++-12
  sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 120 --slave /usr/bin/g++ g++ /usr/bin/g++-12 --slave /usr/bin/gcov gcov /usr/bin/gcov-12
else if [[ $CUDA_VERSION == @(cu125|cu126) ]]; then
  distro=ubuntu2404
  sudo apt install --no-install-recommends gcc-13 g++-13
  sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-13 130 --slave /usr/bin/g++ g++ /usr/bin/g++-13 --slave /usr/bin/gcov gcov /usr/bin/gcov-13
else
    echo "Unsupported CUDA_VERSION: $CUDA_VERSION"
    exit 1
fi

arch=x86_64
wget https://developer.download.nvidia.com/compute/cuda/repos/$distro/$arch/cuda-keyring_1.1-1_all.deb -O cuda-keyring.deb
sudo dpkg -i cuda-keyring.deb

CUDA_SHORT=${CUDA_VERSION:2:2}-${CUDA_VERSION:4:1}
sudo apt update
sudo apt install --no-install-recommends cuda-nvcc-$CUDA_SHORT cuda-libraries-dev-$CUDA_SHORT

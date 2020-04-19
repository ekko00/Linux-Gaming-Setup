#!/bin/bash

#FIXME : Add more distros
echo "[1] Ubuntu / Debian / Debian-based [2] Arch / Manjaro / Arch-based\n"
echo "Select your distro [1/2] -> " 
read op
if [ $op == 1 ];
then
	echo "Installing python and pip"
	sudo apt install python3 python3-pip
	echo "Installing python dependencies"
	pip3 install clint distro pyfiglet --user
elif [ $op == 2 ];
then
	echo "Installing python and pip"
	sudo pacman -S python3 python3-pip python-pip
	echo "Installing python dependencies"
	pip3 install clint distro pyfiglet --user
fi


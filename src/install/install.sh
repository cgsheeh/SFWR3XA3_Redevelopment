#!/bin/sh

# RedevBazaar install script

# Check for root
if [ $(whoami) != "root" ]
	then
		echo "ERROR: Please run as root."
		exit
fi

# Install python and python-dev
sudo apt-get install python
sudo apt-get install python-dev

# Install pyforms dependencies
sudo apt-get install python-setuptools
sudo apt-get install python-opengl
sudo apt-get install python-opencv
sudo apt-get install pyqt4-dev-tools python-qt4
sudo apt-get install python-qt4-gl

# Install pip
sudo python get-pip.py

# Install pyforms
sudo pip install pyforms
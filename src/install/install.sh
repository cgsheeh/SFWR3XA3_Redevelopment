#!/bin/sh

# RedevBazaar install script

# Check for root
if [ $(whoami) != "root" ]
	then
		echo "ERROR: Please run as root."
		exit
fi

# Install python and python-dev
apt-get install python
apt-get install python-dev

# Install pyforms dependencies
#	python-setuptools
#	python-opengl
#	python-opencv
#	pyqt4-dev-tools
#	python-qt4
#	python-qt4-gl
apt-get install python-setuptools
apt-get install python-opengl
apt-get install python-opencv
apt-get install pyqt4-dev-tools python-qt4
apt-get install python-qt4-gl

# Install pip
python get-pip.py

# Install python packages
#	pyforms
#	bitcoin
pip install pyforms
pip install bitcoin
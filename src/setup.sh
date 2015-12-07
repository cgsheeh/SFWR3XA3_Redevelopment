#!/bin/bash

##
# This script will install all required dependencies for 
# the OpenBazaar redevelopment project.
#
# Before running this script, we assume you are on Ubuntu 14
# (ie you have apt-get installed)

##
# First, check for root
if [ $(whoami) != "root" ]
	then
		echo "ERROR: Please run as root (using sudo or some other means).";
		exit;
fi


##
# Find install locations for python and pip, if they are not installed,
# install from apt-get repos
pyth_loc=$(which python)
pip_loc=$(which pip)

if [ $pyth_loc = "" ]
    then
	    apt-get install python;
		
if [ $pip_loc = "" ]
    then
	    apt-get install python-pip;
		
##
# Install Python-dev
# Install PyQt4 (framework for GUI)
apt-get install python-dev
apt-get install python-qt4
		
##
# Check again if programs are installed. If not, exit with a message
pyth_loc=$(which python)
pip_loc=$(which pip)

if [ $pyth_loc = "" ]
    then
	    echo "Python could not be installed using apt-get. Install Python 2.7 and try again.";
		exit
		
if [ $pip_loc = "" ]
    then
	    echo "Pip could not be installed. Install Python-pip and try again.";
		
$pip_loc install -r ob_reqs.txt;
echo "Reqiuirement should now be installed. Run 'python OpenBazaar2.py' to start.";
exit;

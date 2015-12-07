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
pyth_loc=$(which python);
pip_loc=$(which pip);

if [ $pyth_loc = "" ]
    then
        apt-get install python;
        pyth_loc=$(which python);
        if [ $pyth_loc = "" ]
            then
                echo "Python could not be installed using apt-get. Install Python 2.7 and try again.";
                exit;
        fi
fi
		
if [ $pip_loc = "" ]
    then
		echo "\nBEFORE\n";
        $pyth_loc ./install/get-pip.py;
		echo "\nAFTER\N";
        pip_loc=$(which pip);
        if [ $pip_loc = "" ]
            then
                echo "pip could not be installed.";
                exit;
        fi
fi
		
##
# Install Python-dev
# Install PyQt4 (framework for GUI)
apt-get install python-dev;
apt-get install python-qt4;
		
		
$pip_loc install -r reqs.txt;
echo "Reqiuirement should now be installed. Run 'python OpenBazaar2.py' to start.";
exit;
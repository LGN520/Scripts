#!/bin/bash
# switch java version

if [ "x$1" == "x"  ]
then
	sudo update-alternatives --auto java
	sudo update-alternatives --auto javac
	sudo update-alternatives --auto javap
	sudo update-alternatives --auto javah
	sudo update-alternatives --auto jconsole
	sudo update-alternatives --auto jshell
fi

if [ "$1" == "manual"  ]
then
	echo 1 | sudo update-alternatives --config java
	echo 1 | sudo update-alternatives --config javac
	echo 1 | sudo update-alternatives --config javap
	echo 1 | sudo update-alternatives --config javah
	echo 1 | sudo update-alternatives --config jconsole
	echo 1 | sudo update-alternatives --config jshell
fi

if [ "$1" == "display" ]
then
	sudo update-alternatives --display java
	sudo update-alternatives --display javac
	sudo update-alternatives --display javap
	sudo update-alternatives --display javah
	sudo update-alternatives --display jconsole
	sudo update-alternatives --display jshell
fi

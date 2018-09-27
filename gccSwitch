#!/bin/bash
# gcc/g++/gfortran switch

if [ $1 == display ]
then
	echo \n | update-alternatives --config gcc
	echo \n | update-alternatives --config g++
	echo \n | update-alternatives --config gfortran
elif [ $1 == switch ]
then
	gccIdx=$2
	gppIdx=$3
	gfortran=$4
	echo ${gccIdx} |  update-alternatives --config gcc
	echo ${gppIdx} | update-alternatives --config g++
	echo ${gfortran} | update-alternatives --config gfortran

	echo switch success
	gcc --version | head -n 1
	g++ --version | head -n 1
	gfortran --version | head -n 1
fi

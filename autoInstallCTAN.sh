#!/usr/bin/env bash

set -ex

if [ $# != 1 ]
then
	echo "Usage: ./autoInstallCTAN pkgname"
fi

url="http://mirrors.ctan.org/macros/latex/contrib/"$1".zip"
downloadpath="/Users/llgn/Downloads/"
wget $url --directory-prefix=$downloadpath
unzip $downloadpath"/"$1".zip" -d $downloadpath

pkgpath=$downloadpath"/"$1
./installCTAN.sh $pkgpath

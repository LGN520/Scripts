#!/usr/bin/env bash

set -ex

if [ $# != 1 ]
then
	echo "Usage: ./installCTAN.sh pkgpath"
	exit 0
fi

distpath=/usr/local/texlive/2020basic/texmf-dist/tex/latex/

sudo mv $1 $distpath
sudo texhash
sudo mktexlsr

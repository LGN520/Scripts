function convert() {
	dir=$1
	outputdir=$2
	if [ ! -d $outputdir/$dir ]
	then
		mkdir $outputdir/$dir
	fi
	files=($(ls $dir | grep ".pdf"))
	filenum=${#files[@]}
	maxidx=`expr $filenum - 1`
	for i in $(seq 0 $maxidx)
	do
		echo ${files[i]}
		ps2pdf -dPDFSETTINGS=/prepress $dir/${files[i]} $outputdir/$dir/${files[i]}
	done
	echo "Convert $filenum files in $1!"
}

if [ $# != 1 ]
then
	echo "Usage: ./convert.sh output_dir"
	exit
fi

outputdir=$1
if [ ! -d $outputdir ]
then
	mkdir $outputdir
fi

convert "eval" $outputdir
convert "figures" $outputdir

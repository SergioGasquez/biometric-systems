#!/bin/sh

cat pairsDevTest2.txt|while read col1 col2 col3 col4 
do
    if [ -z "$col4" ];then
    	length2=${#col2}
    	if [[ length2 -eq 1 ]];then
    		col2="0"$col2
    	fi
    	length3=${#col3}
    	if [[ length3 -eq 1 ]];then
    		col3="0"$col3
    	fi
    	echo -n 1" "     ;
    	br -algorithm FaceRecognition -compare  ~/Downloads/SBS2/lfw/$col1/$col1"_00"$col2.jpg  ~/Downloads/SBS2/lfw/$col1/$col1"_00"$col3.jpg
    else
    	length2=${#col2}
    	if [[ length2 -eq 1 ]];then
    		col2="0"$col2
    	fi
    	length4=${#col4}
    	if [[ length4 -eq 1 ]];then
    		col4="0"$col4
    	fi
    	echo -n 0" "
    	br -algorithm FaceRecognition -compare  ~/Downloads/SBS2/lfw/$col1/$col1"_00"$col2.jpg  ~/Downloads/SBS2/lfw/$col3/$col3"_00"$col4.jpg
    fi

done

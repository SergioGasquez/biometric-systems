# We import libraries
import os
import sys

from os import listdir
from os.path import isfile, join



image_path = ("C:/Users/sergi/Desktop/SBS/lfw2/")
annotations_path = ("/home/sergio/Downloads/SBS2/pairsDevTrain2.txt")
result_path = ("/home/sergio/Downloads/SBS2/Impaths.txt")



if annotations_path.endswith(".txt"): 
	file = open(annotations_path,'r')
	lines=f.readlines()
	result=[]
	for x in lines:
    	result.append(x.split(' ')[1])
    	print(result)
	f.close()






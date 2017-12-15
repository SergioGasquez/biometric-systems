# We import libraries
import cv2
import os
import sys
import matplotlib

from matplotlib import pyplot as plt # For image printing( I was getting errors with cv2.imshow)
from os import listdir
from os.path import isfile, join

 
# We define the paths of the images, annotations , where we will store the 
# results and the cascade that we will be using

image_path = ("/home/sergio/Downloads/SBS:Exercise/Images/")
annotations_path = ("/home/sergio/Downloads/SBS:Exercise/Annotations/FDDB-folds/")
result_path = ("/home/sergio/Downloads/SBS:Exercise/Results/")
cascadePath = "/home/sergio/.local/share/Trash/files/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"

# We declare our facecascade that we located with the path before
faceCascade = cv2.CascadeClassifier(cascadePath)

# We will go through all the the txt files in annotations folder that contains
# the path for every image,we will open those files one by one,read the path
# of the image and then process the image as explained on bot
for file_name in os.listdir(annotations_path):
	if file_name.endswith(".txt"): 
		file = open(annotations_path+file_name,'r')
		# We create the result.txt file needed for the evaluation program and we
		# open it
		resultfile=file_name[-11:-4]+"-out.txt"
		file2 = open(result_path+resultfile,'w')
		for line in file:
			imagePath= image_path+line[:-1]+".jpg"
			# We write on the output txt the path of the image that we are procesing
			file2.write(line)

			# We read the image and transform it to gray scale so it ligther 
			# to process
			image = cv2.imread(imagePath)
			gray= cv2.imread(imagePath,cv2.IMREAD_GRAYSCALE)
			# We use the funciton detectMultiScale in order to locate faces
			# and have the confident score

			faces,rejectLevels,levelWeights = faceCascade.detectMultiScale3(
				gray,			# Input image
			 	scaleFactor=1.1, # Donwsized image ratio
			 	minNeighbors=4,	# Min of neigthbors that should say that there is a face
			 	flags = cv2.CASCADE_SCALE_IMAGE, # Similar to cv2.cv.CV_HAAR_SCALE_IMAGE
			 	minSize = (30, 30), # Min size of the face
			 	maxSize = (500,500),# Max size of the face
			  	outputRejectLevels =True		# That will give us rejectLevels and levelWeights outputs
			 	)	

			# We define the font that we will use to print the confident score
			font = cv2.FONT_HERSHEY_SIMPLEX
			# We will use a variable(i) to print the confident score,since
			# levelWeigths is an array which length is equal to the number of 
			# faces detected
			i = 0
			# We write on the output txt the number of faces on the image
			file2.write("%d \n" % len(faces))
			# We go trougth the faces matrix and print rectangles and confident score
			for (x, y, w, h) in faces:
				 # If we want to print the rectangle and the confident score
				 # on the image we only have to uncomment the following two lines:
			     #cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
			     #cv2.putText(image,str(levelWeights[i]),(x,y - 8), font, 0.5, (0,255,0), 1, cv2.LINE_AA)
			     file2.write("%d %d %d %d %f \n" % (x,y,w,h,levelWeights[i]))
			     i = i + 1



# We can save the image in a file or print it by uncommenting those lines:
#cv2.imwrite("/home/sergio/Downloads/SBS:Exercise/Saves/prueba.jpg",image)
#cv2.imshow("Original",image)
#plt.imshow(image, cmap = 'gray', interpolation = 'bicubic')
#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#plt.show()


# Like it says in the statement,we have an option to have and resized output
scaledOutput = 0
if  scaledOutput:
	rescaledImage = cv2.resize(image,None,fx=2, fy=2, interpolation = cv2.INTER_LINEAR)
#	cv2.imwrite("/home/sergio/Downloads/SBS:Exercise/Saves/pruebaScaled.jpg",image)
#	cv2.imshow("Resized",rescaledImage)
#	plt.imshow(rescaledImage, cmap = 'gray', interpolation = 'bicubic')
#	plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#	plt.show()

# Face Matching

## Requirements
### Pipeline1
* [OpenBR](http://openbiometrics.org/)
* [LFW dataset](http://vis-www.cs.umass.edu/lfw/)
* [LIBLINEAR](http://www.csie.ntu.edu.tw/~cjlin/cgi-bin/liblinear.cgi?+http://www.csie.ntu.edu.tw/~cjlin/liblinear+zip)
### Pipeline2
* [PhD face recognition toolbox](http://luks.fe.uni-lj.si/sl/osebje/vitomir/face_tools/PhDface/)
* [LFW-A dataset](http://www.openu.ac.il/home/hassner/data/lfwa/)

## Usage
### Pipeline1
We must use the shell script and save the output into a .txt.Then,to evaluate
we will use a matlab script in order to obtan the ROC.

### Pipeline 2
First we need to adapt both python scripts and readjust the paths.Then we will
run ImpathsTrain and save the output int a .txt 
```{r, engine='sh', count_lines}
$ python ImpathsTrain.py > 'Paths.txt'
```
We need to install PhD face recognition toolbox on Matlab following the Readme that
comes with it.Then we will crop all the images using Matlab script Crop.m by just
taking as input the previusly generated .txt and running it.

Again,we will use a python script(obtainPaths) to get all the paths of the
images pairs given in both  pairsDevTrain.txt and pairsDevTest.txt.
Finally you just have to adjust paths and run the Matlab script Task5.m

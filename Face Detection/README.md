# Face Recognition Script

## Requirements
* [OpenCV 3](https://opencv.org/opencv-3-0.html)
* [Face Detection Data Set and Benchmark (FDDB)](http://vis-www.cs.umass.edu/fddb/)
* [Scoring program](http://vis-www.cs.umass.edu/fddb/evaluation.tgz)

## Usage
First,we need to readjust the python script paths.Then you can run the script saving the output into a txt with:
```{r, engine='sh', count_lines}
$ python FaceDetector.py > Output.txt
```

## Running tests
To evaluate we need to compile the scoring program and run it:
```{r, engine='sh', count_lines}
$ cd <scoring program>
$ make
$ ./runEvaluate
```
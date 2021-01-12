# KNN

This repository include an implementation of the KNN algorithm in python. 

## Submitters: 

Yishay Seroussi 305027948, Samuel Bismuth 342533064.

## Python version:

 3.9

## Configuration

This repository includes an implementation of the knn alogithm in python.

We use the docker environement. Make sure docker is installed in you machine. That is the only dependency of the project. 

According to your distribution, run:

    sudo <yum/apt-get> install -y docker

Then, to run the script run: 
    
    bash start.sh 

To enter in the container terminal (only for developement purpose):

    bash bash.sh 

If you don't want to use docker, you are able to run the code in any machine by folowing the next steps:

Install python3.9.

Install numpy by running:

    pip3 install numpy
    pip3 install sklearn

Run the main python file:

    python3 main.py

## Code structure:

The code is composed of three folders.

- The data folder containing the txt file of data received for the assignment.
- The packages folder containing the requirement txt file with the pip lib we used (numpy, sklearn).
- The src folder containing the code source.
    - main.py -> The main file of the code. This is our entrypoint. This is also the file were the prints are done.
    - data.py -> The file handle the txt data to convert it into objects.
    - knn.py -> Here you can find the main algorithm with the computation of the final error and error.

## Example of outputs:

#################################################### <br>
Train -> k: 1, p: 1, error: 0.4646153846153844 <br>
Test -> k: 1, p: 1, error: 0.0281538461538461 <br>
#################################################### <br>

#################################################### <br>
Train -> k: 1, p: 2, error: 0.46753846153846135 <br>
Test -> k: 1, p: 2, error: 0.027538461538461498 <br>
#################################################### <br>

#################################################### <br>
Train -> k: 1, p: inf, error: 0.4684615384615384 <br>
Test -> k: 1, p: inf, error: 0.029384615384615315 <br>
#################################################### <br>

#################################################### <br>
Train -> k: 3, p: 1, error: 0.43907692307692286 <br>
Test -> k: 3, p: 1, error: 0.2215384615384611 <br>
#################################################### <br>

#################################################### <br>
Train -> k: 3, p: 2, error: 0.449076923076923 <br>
Test -> k: 3, p: 2, error: 0.23507692307692274 <br>
#################################################### <br>

#################################################### <br>
Train -> k: 3, p: inf, error: 0.45523076923076905 <br>
Test -> k: 3, p: inf, error: 0.2338461538461535 <br>
#################################################### <br>

#################################################### <br>
Train -> k: 5, p: 1, error: 0.45276923076923054 <br>
Test -> k: 5, p: 1, error: 0.28615384615384576 <br>
#################################################### <br>

#################################################### <br>
Train -> k: 5, p: 2, error: 0.4484615384615382 <br>
Test -> k: 5, p: 2, error: 0.2855384615384612 <br>
#################################################### <br>

#################################################### <br>
Train -> k: 5, p: inf, error: 0.4639999999999997 <br>
Test -> k: 5, p: inf, error: 0.2881538461538458 <br>
#################################################### <br>

#################################################### <br>
Train -> k: 7, p: 1, error: 0.46384615384615374 <br>
Test -> k: 7, p: 1, error: 0.3186153846153842 <br>
#################################################### <br>

#################################################### <br>
Train -> k: 7, p: 2, error: 0.4921538461538462 <br>
Test -> k: 7, p: 2, error: 0.3075384615384611 <br>
#################################################### <br>

#################################################### <br>
Train -> k: 7, p: inf, error: 0.47123076923076906 <br>
Test -> k: 7, p: inf, error: 0.3112307692307688 <br>
#################################################### <br>

#################################################### <br>
Train -> k: 9, p: 1, error: 0.4693846153846152 <br>
Test -> k: 9, p: 1, error: 0.3426153846153842 <br>
#################################################### <br>

#################################################### <br>
Train -> k: 9, p: 2, error: 0.4823076923076924 <br>
Test -> k: 9, p: 2, error: 0.3489230769230766 <br>
#################################################### <br>

#################################################### <br>
Train -> k: 9, p: inf, error: 0.48784615384615376 <br>
Test -> k: 9, p: inf, error: 0.3447692307692304 <br>
#################################################### <br>

## Work division

We worked on this code together using one computer as a pair programming.
That is, we've handle and understand together the complexity of the knn implementation and the code design in python. There is nothing in this work that have been done only by one submitter.
Notice that we worked only on one github account since we used only one computer.
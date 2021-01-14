#!/bin/bash

sudo docker build -t knn . 

sudo docker run --rm -it knn

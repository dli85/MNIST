# MNIST

## Overview

Mnist is a keras dataset that contains tens of thousands of images of digits. The "goal" of the dataset is to create a program that can look the images and tell which digit the image is displaying. The images are 28x28 pixles.

To accomplish this task, we will use a simple neural network. We first extract the dataset from the keras library into python lists. The lists contain the numerical values for the images. To view the actual images, we will need to use matplotlib. The lists are in the shape of 28 by 28 as those are the dimensions of the images. To feed the data into the model, we need to flatten them. We can do this by either adding a layer to our model or reshaping the lists beforehand. Once all the data preparation is done, we can train the model.

## Usage

The mnistTrain.py file extracts the data and trains the model. When finished, the model will be saved as model.h5 to the same folder as the mnistTrain.py file is in

The mnistTest.py file tests the model's accuracy on the testing data and displays the images as well as the model's predictions

## Requirements

Use pip to install the required libraries:

```bash
pip install tensorflow matplotlib numpy
```

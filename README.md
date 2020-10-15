# MNIST

## Overview

Mnist is a keras dataset that contains tens of thousands of images of digits. The images are 28x28 and the goal is to train a model to recognize the which images corrospond to which 
numbers. 

To do this, we first extract the dataset from the keras library into python lists. The lists contain the numerical values for the images. To view the actual images, matplotlib is needed.
The lists are in the shape of 28 by 28. To feed the data into the model, we need to flatten them. We can do this by either adding a layer to our model or reshaping the lists
beforehand. Once all the data preparation is done, we can train the model.

## Usage

The mnistTrain.py file extracts the data and trains the model. When finished, the model will be saved as model.h5 to the same folder as the mnistTrain.py file is in

The mnistTest.py file tests the model's accuracy on the testing data and displays the images as well as the model's predictions

## Requirements

Use pip to install the requirements

```bash
pip install tensorflow matplotlib numpy
```

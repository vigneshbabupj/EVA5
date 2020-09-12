# EVA - Assignment 7 - CIFAR10 image Classification

Convolution neural network designed to clasify the images of the CIFAR-10 dataset in Pytorch

> The CIFAR-10 dataset consists of 60000 32x32 colour images in 10 classes, with 6000 images per class. There are 50000 training images and 10000 test images

# Problem Statement
Change the given network as per the below instructions
* change the code such that it uses GPU
* change the architecture to C1C2C3C40 (basically 3 MPs)
* total RF must be more than 44
* one of the layers must use Depthwise Separable Convolution
* one of the layers must use Dilated Convolution
* use GAP (compulsory):- add FC after GAP to target #of classes (optional)
* achieve 80% accuracy, as many epochs as you want. Total Params to be less than 1M. 

# Model Architecture

![image](https://user-images.githubusercontent.com/48342398/92998408-481ba880-f537-11ea-907a-2b79293d32ae.png)



# Model Hyperparamters
* Batch size - 128
* Epochs - 20
* optimizer - Stochastic Gradient decent with lr 0.01
* Loss function - Crossentropy loss

# Result:
* Parameters: 975,296
* Train Accuracy - 95.5%
* Test Accuracy - 83.8%

# Class wise accuracy
* Accuracy of plane : 96 %
* Accuracy of   car : 93 %
* Accuracy of  bird : 73 %
* Accuracy of   cat : 56 %
* Accuracy of  deer : 88 %
* Accuracy of   dog : 62 %
* Accuracy of  frog : 90 %
* Accuracy of horse : 96 %
* Accuracy of  ship : 92 %
* Accuracy of truck : 96 %

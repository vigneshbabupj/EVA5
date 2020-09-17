# EVA - Assignment 8 - CIFAR10 image Classification

Convolution neural network designed to clasify the images of the CIFAR-10 dataset in Pytorch

> The CIFAR-10 dataset consists of 60000 32x32 colour images in 10 classes, with 6000 images per class. There are 50000 training images and 10000 test images

# Problem Statement
Change the given network as per the below instructions
* Go through this repository: https://github.com/kuangliu/pytorch-cifar
* Extract the ResNet18 model from this repository and add it to your API/repo. 
* Use your data loader, model loading, train, and test code to train ResNet18 on Cifar10
* Your Target is 85% accuracy. No limit on the number of epochs. Use default ResNet18 code (so params are fixed). 

# Model

ResNet18

![image](https://user-images.githubusercontent.com/48342398/93422153-c1692180-f8d0-11ea-99c2-86efd79c16f0.png)



# Model Hyperparamters
* Batch size - 128
* Epochs - 100
* optimizer - Stochastic Gradient decent with lr 0.01
* Loss function - Crossentropy loss

# Result:
* Parameters: 11,173,962
* Train Accuracy - 99.684% (100th epoch)
* Test Accuracy - 92.6% (100th epoch)

# Class wise accuracy
* Accuracy of plane : 94 %
* Accuracy of   car : 89 %
* Accuracy of  bird : 95 %
* Accuracy of   cat : 90 %
* Accuracy of  deer : 96 %
* Accuracy of   dog : 76 %
* Accuracy of  frog : 91 %
* Accuracy of horse : 95 %
* Accuracy of  ship : 100 %
* Accuracy of truck : 100 %

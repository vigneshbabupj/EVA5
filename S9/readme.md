# EVA - Assignment 9 - CIFAR10 image Classification

Convolution neural network designed to clasify the images of the CIFAR-10 dataset in Pytorch

> The CIFAR-10 dataset consists of 60000 32x32 colour images in 10 classes, with 6000 images per class. There are 50000 training images and 10000 test images

# Problem Statement
Change the given network as per the below instructions
1. Move your last code's transformations to Albumentations. Apply ToTensor, HorizontalFlip, Normalize (at min) + More (for additional points)
2. Please make sure that your test_transforms are simple and only using ToTensor and Normalize
3. Implement GradCam function as a module. 
4. Your final code (notebook file) must use imported functions to implement transformations and GradCam functionality
5. Target Accuracy is 87%
6. Submit answers to S9-Assignment-Solution. 

# Model

ResNet18

![image](https://user-images.githubusercontent.com/48342398/93422153-c1692180-f8d0-11ea-99c2-86efd79c16f0.png)



#Albumentations Transformations applied
* HorizontalFlip
* Normalize
* Cutout
* ToTensor

# Model Hyperparamters
* Batch size - 128
* Epochs - 50
* optimizer - Stochastic Gradient decent with lr 0.01
* Loss function - Crossentropy loss

# Result:
* Parameters: 11,173,962
* Train Accuracy - 96.684% (100th epoch)
* Test Accuracy - 88.6% (100th epoch)

# Model Performance


#GradCam Results
Gradcam results at 4 layers for random 5 images:


#InCorrect Classifications
Sample images which are incorreclty classified:



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

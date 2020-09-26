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
* Train Accuracy - 98.2% (50th epoch)
* Test Accuracy - 88.7% (50th epoch)

# Model Performance

![image](https://user-images.githubusercontent.com/48342398/94346183-8e4d2d80-0048-11eb-9853-df5c819742dc.png)


#GradCam Results
Gradcam results at 4 layers for random 5 images:

![image](https://user-images.githubusercontent.com/48342398/94346201-a8870b80-0048-11eb-848e-ef1bc9289aab.png)


#InCorrect Classifications
Sample images which are incorreclty classified:

![image](https://user-images.githubusercontent.com/48342398/94346323-7de98280-0049-11eb-90bc-0575ddf600af.png)


# Class wise accuracy

* Accuracy of plane : 94 %
* Accuracy of   car : 95 %
* Accuracy of  bird : 75 %
* Accuracy of   cat : 83 %
* Accuracy of  deer : 97 %
* Accuracy of   dog : 86 %
* Accuracy of  frog : 93 %
* Accuracy of horse : 90 %
* Accuracy of  ship : 100 %
* Accuracy of truck : 97 %

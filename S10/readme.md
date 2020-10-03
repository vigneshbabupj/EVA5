# EVA - Assignment 10 - CIFAR10 image Classification

Convolution neural network designed to clasify the images of the CIFAR-10 dataset in Pytorch

> The CIFAR-10 dataset consists of 60000 32x32 colour images in 10 classes, with 6000 images per class. There are 50000 training images and 10000 test images

# Problem Statement
Change the given network as per the below instructions
1. Pick your last code
2. Make sure  to Add CutOut to your code. It should come from your transformations (albumentations)
	1. Use this repo: https://github.com/davidtvs/pytorch-lr-finder
	2. Move LR Finder code to your modules
	3. Implement LR Finder (for SGD, not for ADAM)
4. Implement ReduceLROnPlatea: https://pytorch.org/docs/stable/optim.html#torch.optim.lr_scheduler.ReduceLROnPlateau
5. Find best LR to train your model
6. Use SDG with Momentum
7. Train for 50 Epochs. 
8. Show Training and Test Accuracy curves
8. Target 88% Accuracy.
9. Run GradCAM on the any 25 misclassified images. Make sure you mention what is the prediction and what was the ground truth label.
10. Submit

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
* Train Accuracy - 98.97% (50th epoch)
* Test Accuracy - 90.84% (50th epoch)

# Model Performance

![image](https://user-images.githubusercontent.com/48342398/94986052-1b2c4580-0579-11eb-8a09-d480abdf334b.png)



#GradCam Results 25 misclassified images


![image](https://user-images.githubusercontent.com/48342398/94986066-31d29c80-0579-11eb-8495-44e74343935c.png)



#InCorrect Classifications
Sample images which are incorreclty classified:

![image](https://user-images.githubusercontent.com/48342398/94986078-49aa2080-0579-11eb-82a5-37430e5df643.png)


# Class wise accuracy

* Accuracy of plane : 91 %
* Accuracy of   car : 95 %
* Accuracy of  bird : 96 %
* Accuracy of   cat : 91 %
* Accuracy of  deer : 92 %
* Accuracy of   dog : 91 %
* Accuracy of  frog : 86 %
* Accuracy of horse : 97 %
* Accuracy of  ship : 92 %
* Accuracy of truck : 100 %

# EVA - Assignment 11 - CIFAR10 image Classification

Convolution neural network designed to clasify the images of the CIFAR-10 dataset in Pytorch

> The CIFAR-10 dataset consists of 60000 32x32 colour images in 10 classes, with 6000 images per class. There are 50000 training images and 10000 test images

## Problem Statement
Change the given network as per the below instructions
1. Write a code that draws this curve (without the arrows). In submission, you'll upload your drawn curve and code for that
2. Write a code which 
	1. uses this new ResNet Architecture for Cifar10:
		1. PrepLayer - 
			1. Conv 3x3 s1, p1) >> BN >> RELU [64k]
		2. Layer1 -
			1. X = Conv 3x3 (s1, p1) >> MaxPool2D >> BN >> RELU [128k]
			2. R1 = ResBlock( (Conv-BN-ReLU-Conv-BN-ReLU))(X) [128k] 
			3. Add(X, R1)
		3. Layer 2 -
			1. Conv 3x3 [256k]
			2. MaxPooling2D
			3. BN
			4. ReLU
		4. Layer 3 -
			1. X = Conv 3x3 (s1, p1) >> MaxPool2D >> BN >> RELU [512k]
			2. R2 = ResBlock( (Conv-BN-ReLU-Conv-BN-ReLU))(X) [512k]
			3. Add(X, R2)
		5. MaxPooling with Kernel Size 4
		6. FC Layer 
		7. SoftMax
	2. Uses One Cycle Policy such that:
		1. Total Epochs = 24
		2. Max at Epoch = 5
		3. LRMIN = FIND
		4. LRMAX = FIND
		5. NO Annihilation
	3. Uses this transform -RandomCrop 32, 32 (after padding of 4) >> FlipLR >> Followed by CutOut(8, 8)
	4. Batch size = 512
	5. Target Accuracy: 90%. 
	6. The lesser the modular your code is (i.e. more the code you have written in your Colab file), less marks you'd get. 


## Lr change curve

![image](https://user-images.githubusercontent.com/48342398/95652062-14b74400-0b0c-11eb-8379-5b4b0306abc8.png)



## Model Summary

![image](https://user-images.githubusercontent.com/48342398/95651801-53e49580-0b0a-11eb-814a-f966c2eed47f.png)




## Lr Range Test

![image](https://user-images.githubusercontent.com/48342398/95651871-c5bcdf00-0b0a-11eb-997a-c7510885deaa.png)




## Model Hyperparamters
* Batch size - 512
* Epochs - 24
* optimizer - Stochastic Gradient decent
	* Max Lr : 0.01
	* Min Lr : 0.001
* Loss function - NLL loss

## Lr Change during training

![image](https://user-images.githubusercontent.com/48342398/95651915-0ae11100-0b0b-11eb-8862-edb34146f455.png)


## Result:
* Parameters: 6,573,130
* Train Accuracy - 96.108% (24th epoch)
* Test Accuracy - 90.06% (24th epoch)

## Model Performance

![image](https://user-images.githubusercontent.com/48342398/95651982-7dea8780-0b0b-11eb-917d-be8400273b08.png)




## InCorrect Classifications
Sample images which are incorreclty classified:

![image](https://user-images.githubusercontent.com/48342398/95652015-b7bb8e00-0b0b-11eb-9dde-e563ad02d859.png)



## Class wise accuracy

* Accuracy of plane : 87 %
* Accuracy of   car : 90 %
* Accuracy of  bird : 100 %
* Accuracy of   cat : 100 %
* Accuracy of  deer : 100 %
* Accuracy of   dog : 66 %
* Accuracy of  frog : 84 %
* Accuracy of horse : 75 %
* Accuracy of  ship : 90 %
* Accuracy of truck : 100 %

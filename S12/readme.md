# EVA - Assignment 12 - ResNet18 model on Tiny Imagenet dataset


## Problem Statement
1. Assignment A:
	1. Download this [TINY IMAGENET](http://cs231n.stanford.edu/tiny-imagenet-200.zip) dataset.
	2. Train ResNet18 on this dataset (70/30 split) for 50 Epochs. Target 50%+ Validation Accuracy. 
	3. Submit Results. Of course, you are using your own package for everything. You can look at [this](https://github.com/sonugiri1043/Train_ResNet_On_Tiny_ImageNet/blob/master/Train_ResNet_On_Tiny_ImageNet.ipynb)  for reference. 
2.	Assignment B:
	1. Download 50 (min) images each of people wearing hardhat, vest, mask and boots. 
	2. Use these labels (same spelling and small letters):
		* hardhat
		* vest
		* mask
		* boots
	3. Use [this](http://www.robots.ox.ac.uk/~vgg/software/via/via_demo.html) to annotate bounding boxes around the hardhat, vest, mask and boots.
	4. Download JSON file. 
	5. Describe the contents of this JSON file in FULL details (you don't need to describe all 10 instances, anyone would work). 
	6. Refer to this [tutorial](https://towardsdatascience.com/machine-learning-algorithms-part-9-k-means-example-in-python-f2ad05ed5203) . Find out the best total numbers of clusters. Upload link to your Colab File uploaded to GitHub. 


## Assingment A

Final file: https://github.com/vigneshbabupj/EVA5/blob/master/S12/S12_Assignment_B/EVA_A12_A_Final.ipynb
 
### Model Summary

ResNet18 Model:

![image](https://user-images.githubusercontent.com/48342398/96336670-071b3480-109f-11eb-9afb-1ca6777bbdc1.png)


### Lr Range Test

![image](https://user-images.githubusercontent.com/48342398/96336689-23b76c80-109f-11eb-9af5-3cca655e690d.png)


### Model Hyperparamters
* Batch size - 256
* Epochs - 50
* optimizer - Stochastic Gradient decent
	* Max Lr : 0.05
	* Min Lr : 0.005
* Loss function - CrossEntropyLoss

### Lr Change during training

![image](https://user-images.githubusercontent.com/48342398/96336706-55c8ce80-109f-11eb-85d9-a9f61ebce63f.png)



### Result:
* Parameters: 11,271,432
* Train Accuracy - 99.43% (50th epoch)
* Test Accuracy - 61.62% (50th epoch)

### Model Performance

![image](https://user-images.githubusercontent.com/48342398/96336864-18187580-10a0-11eb-9957-bcdad93c50a0.png)



##  Assingment B


Images: https://github.com/vigneshbabupj/EVA5/tree/master/S12/S12_Assignment_B/S12_photos 

Annotation Json file: https://github.com/vigneshbabupj/EVA5/blob/master/S12/S12_Assignment_B/S12photos_images_json.json 

K Means clustering: https://github.com/vigneshbabupj/EVA5/blob/master/S12/S12_Assignment_B/EVA_A12_B.ipynb

* No of clusters identified = 5

![image](https://user-images.githubusercontent.com/48342398/96251588-50e81a00-0fce-11eb-9688-eeeb7e9efda2.png)

# EVA - Assignment 12


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

Final file: 
 
### Model Summary


### Lr Range Test



### Model Hyperparamters
* Batch size - 256
* Epochs - 50
* optimizer - Stochastic Gradient decent
	* Max Lr : 0.03
	* Min Lr : 0.003
* Loss function - CrossEntropyLoss

### Lr Change during training



### Result:
* Parameters: 11,271,432
* Train Accuracy - 96.108% (24th epoch)
* Test Accuracy - 90.06% (24th epoch)

### Model Performance



### InCorrect Classifications
Sample images which are incorreclty classified:


##  Assingment B


Images: https://github.com/vigneshbabupj/EVA5/tree/master/S12/S12_Assignment_B/S12_photos 

Annotation Json file: https://github.com/vigneshbabupj/EVA5/blob/master/S12/S12_Assignment_B/S12photos_images_json.json 

K Means clustering: https://github.com/vigneshbabupj/EVA5/blob/master/S12/S12_Assignment_B/EVA_A12_B.ipynb

* No of clusters identified = 5

![image](https://user-images.githubusercontent.com/48342398/96251588-50e81a00-0fce-11eb-9688-eeeb7e9efda2.png)

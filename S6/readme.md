# EVA - Assignment 6 - Various Regularization Effect

Convolution neural network designed to clasify the images of the MNIST dataset in Pytorch

> The MNIST dataset (Modified National Institute of Standards and Technology database) is a large database of handwritten digits that is commonly used for training various image processing systems.

# Problem Statement
Run code with below version of network and report findings
* with L1 + BN
* with L2 + BN
* with L1 and L2 with BN
* with GBN
* with L1 and L2 with GBN

# Code
 Single Loop to run different versions of the model for 25 epochs and save them.
 The below configuration is used for different versions
*L1+BN:{'lambda_l1':0.01,'lambda_l2':0,'Batch_Norm':"BN"},
* L2+BN:{'lambda_l1':0,'lambda_l2':0.01,'Batch_Norm':"BN"},
* L1+L2+BN:{'lambda_l1':0.01,'lambda_l2':0.01,'Batch_Norm':"BN"},
* GBN:{'lambda_l1':0,'lambda_l2':0,'Batch_Norm':"GBN"},
* L1+L2+GBN:{'lambda_l1':0.01,'lambda_l2':0.01,'Batch_Norm':"GBN"}

# Findings:

The below is the comparison of Validation Accuracy:

![image](https://user-images.githubusercontent.com/48342398/91642910-bf880d00-ea4c-11ea-8a3d-05c611100275.png)


The below is the comparison of Validation Loss:

![image](https://user-images.githubusercontent.com/48342398/91642942-ef371500-ea4c-11ea-8ec3-7d2d08ffcf2b.png)

25 misclassified Images of GBN:



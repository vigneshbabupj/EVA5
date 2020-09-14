# EVA - Assignment 4 - MNIST Classification problem

By:
  - Vignesh Babu P J -> vigneshbabupj@gmail.com
  - Srivatsan -> srivatsanmurugan96@gmail.com
  - Ravi Shankar- > ravishankar2k4@gmail.com
  - Siddartha -> lezaroth3@gmail.com

Convolution neural network designed to clasify the images of the MNIST dataset in Pytorch

> The MNIST dataset (Modified National Institute of Standards and Technology database) is a large database of handwritten digits that is commonly used for training various image processing systems.

# Architecture 
The Architecure encompess the following blocks:

 ### Convolution Block 1 
  - 3 layers of 3x3 Convolution
  - Each layers consits of Batch Normalization
  - Each layer also consits of Dropout(0.1)
  - The no of channels used is 16
 
 ### Transistion Block 1
  - Max pooling with Size 2 and stride 2
  - 1x1 Convolution to readuce the channel size from 16 to 8 

 ### Convolution Block 2
   - 3 layers of 3x3 Convolution
   - Each layers consits of Batch Normalization
  - Each layer also consits of Dropout(0.1)
  - The no of channels used in this block is 16
  
  ### Transistion Block 2
  - Global Average pooling is used before the last layer to include features identifed in multiple channels
  - 3x3 Convolution is used as last layer to get the 10 classes of output
  - Log Softmax is used to determine the likelihood of the each of the digit from the image
 
# Optimizer
SGD is used as the optimizer with a learning rate of 0.01 and momentum of 0.9

# Training
 - Batch Size - 64 
 - No of paramters - 11,106
 - no of Epochs - 20
 - highest Validation Accuracy - 99.45% ( 19th epoch) 


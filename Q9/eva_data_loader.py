# -*- coding: utf-8 -*-
"""EVA_Data_Loader.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Fj6T8HLiPowkwDvzeVKmf1mHdXA74AWe
"""

from tqdm import tqdm
import torch 
import torch.nn as nn
from torchvision import datasets, transforms
from torchsummary import summary
import torch.nn.functional as F
import torch.optim as optim

def MNIST_dataloader(Batch_size, use_cuda):

  # Train Phase transformations
  train_transforms = transforms.Compose([
                                        #  transforms.Resize((28, 28)),
                                        #  transforms.ColorJitter(brightness=0.10, contrast=0.1, saturation=0.10, hue=0.1),
                                        transforms.RandomRotation((-7.0, 7.0), fill=(1,)),
                                        transforms.ToTensor(),
                                        transforms.Normalize((0.1307,), (0.3081,)) # The mean and std have to be sequences (e.g., tuples), therefore you should add a comma after the values. 
                                        # Note the difference between (0.1307) and (0.1307,)
                                        ])

  # Test Phase transformations
  test_transforms = transforms.Compose([
                                        #  transforms.Resize((28, 28)),
                                        #  transforms.ColorJitter(brightness=0.10, contrast=0.1, saturation=0.10, hue=0.1),
                                        transforms.ToTensor(),
                                        transforms.Normalize((0.1307,), (0.3081,))
                                        ])


  #Get the MNIST dataset

  train_dataset =  datasets.MNIST('/data/', train=True, download=True,
                              transform=train_transforms)


  test_dataset =  datasets.MNIST('/data/', train=False, download=True,
                              transform=test_transforms) 
  
    
  dataloader_args= dict(shuffle=True, batch_size=Batch_size,num_workers=4, pin_memory=True ) if use_cuda else dict(shuffle=True, batch_size=Batch_size)

  train_loader = torch.utils.data.DataLoader(train_dataset, **dataloader_args)

  test_loader = torch.utils.data.DataLoader(test_dataset, **dataloader_args)


  return train_loader,test_loader

def CIFAR10_dataloader(Batch_size, use_cuda):

  # Train Phase transformations
  train_transforms = transforms.Compose([
                                        #  transforms.Resize((28, 28)),
                                        #  transforms.ColorJitter(brightness=0.10, contrast=0.1, saturation=0.10, hue=0.1),
                                        # transforms.RandomRotation((-7.0, 7.0), fill=(1,)),
                                        transforms.RandomHorizontalFlip(p=0.5),
                                        transforms.ToTensor(),
                                        transforms.Normalize((0.4890062, 0.47970363, 0.47680542), (0.264582, 0.258996, 0.25643882)) 
                                        ])

  # Test Phase transformations
  test_transforms = transforms.Compose([
                                        #  transforms.Resize((28, 28)),
                                        #  transforms.ColorJitter(brightness=0.10, contrast=0.1, saturation=0.10, hue=0.1),
                                        transforms.ToTensor(),
                                        transforms.Normalize((0.4890062, 0.47970363, 0.47680542), (0.264582, 0.258996, 0.25643882))
                                        ])


  #Get the MNIST dataset

  train_dataset =  datasets.CIFAR10('/data/', train=True, download=True,
                              transform=train_transforms)


  test_dataset =  datasets.CIFAR10('/data/', train=False, download=True,
                              transform=test_transforms) 
  
   
  dataloader_args= dict(shuffle=True, batch_size=Batch_size,num_workers=4, pin_memory=True ) if use_cuda else dict(shuffle=True, batch_size=Batch_size)

  train_loader = torch.utils.data.DataLoader(train_dataset, **dataloader_args)

  test_loader = torch.utils.data.DataLoader(test_dataset, **dataloader_args)

  classes = ('plane', 'car', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck')


  return train_loader,test_loader, classes
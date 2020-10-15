

import albumentations as A
from albumentations.pytorch import ToTensorV2
#from albumentations.pytorch.transforms import ToTensor

from torchvision import datasets, transforms
import numpy as np


class AlbumentationImageDataset():
  def __init__(self,transform):
      #self.image_list = image_list
      self.aug = transform

  def __call__(self, img):
    img = np.array(img)

    return self.aug(image=img)['image']
        


class MNIST_Albumentation():
  def __init__(self):
      self.mean = 0.1307
      self.std = 0.3081
      
      self.train_transforms = A.Compose([
                                  A.Rotate(limit=90, interpolation=1, border_mode=4, value=None, mask_value=None, always_apply=False, p=0.5),
                                  A.Normalize(
                                      mean= self.mean,
                                      std=self.std,
                                      ),
                                  ToTensorV2()
                                  #ToTensor()
                                  ])
      self.test_transforms = A.Compose([
                                  A.Normalize(
                                        mean = self.mean,
                                        std = self.std,
                                        ),
                                  ToTensorV2()
                                  #ToTensor()
                                  ])
    
    
  def __call__(self,is_train):
    if is_train == True:
        return AlbumentationImageDataset(self.train_transforms)
    else:
        return AlbumentationImageDataset(self.test_transforms)
  
  
class CIFAR10_Albumentation():
  def __init__(self):
      self.mean = [0.4890062, 0.47970363, 0.47680542]
      self.std = [0.264582, 0.258996, 0.25643882]

      self.train_transforms = A.Compose([
                                  A.HorizontalFlip(p=0.5),
                                  A.Normalize(
                                      mean = self.mean,
                                      std= self.std,
                                      ),
                                  A.Cutout ( num_holes=1, max_h_size=16, max_w_size=16,  fill_value= self.mean, always_apply=False, p=0.5),
                                  ToTensorV2()
                                  #ToTensor()
                                  ])
                                  
      self.test_transforms = A.Compose([

                                  A.Normalize(
                                      mean = self.mean,
                                      std = self.std,
                                      ),
                                  ToTensorV2()
                                  #ToTensor()
                                  ])

  def __call__(self,is_train):
    if is_train == True:
        return AlbumentationImageDataset(self.train_transforms)
    else:
        return AlbumentationImageDataset(self.test_transforms)
        
        


class CIFAR10_A11_transformation():
  def __init__(self):
      self.mean = [0.4890062, 0.47970363, 0.47680542]
      self.std = [0.264582, 0.258996, 0.25643882]

      self.train_transforms = A.Compose([
      
                                  A.PadIfNeeded(min_height=40, min_width=40, always_apply=True),
                                  A.RandomCrop(height=32, width=32, always_apply=True),
                                  A.HorizontalFlip(p=0.5),
                                  A.Cutout( num_holes=1, max_h_size=8, max_w_size=8, fill_value= self.mean, always_apply=False, p=0.5),
                                  
                                  A.Normalize( mean = self.mean, std= self.std,),                                  
                                  ToTensorV2()
                                  #ToTensor()
                                  ])
                                  
      self.test_transforms = A.Compose([

                                  A.Normalize( mean = self.mean, std= self.std,),                                  
                                  ToTensorV2()
                                  #ToTensor()
                                  ])

  def __call__(self,is_train):
    if is_train == True:
        return AlbumentationImageDataset(self.train_transforms)
    else:
        return AlbumentationImageDataset(self.test_transforms)
        

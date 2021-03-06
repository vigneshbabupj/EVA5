# -*- coding: utf-8 -*-
"""EVA_Regularization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JoRG643NERtjxqx20COF1xf3iHzHbQoj
"""

import torch 
import torch.nn as nn
import torch.nn.functional as F

def get_l1_loss(model,lambda_l1):
    # L1 Regularization
    l1=0
    for p in model.parameters():
      l1=l1+p.abs().sum()
    
    l1_loss=lambda_l1*l1

    return l1_loss

class Dropout(nn.Module):
    def __init__(self, val):
        super(Dropout, self).__init__()
        self.drop = nn.Dropout(val)

    def forward(self, x):
        x = self.drop(x)
        return x
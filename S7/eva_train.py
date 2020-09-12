# -*- coding: utf-8 -*-
"""EVA_Train.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18HFbmMoIDd2bDkysIyoIfXdhU8DMehwg
"""

from tqdm import tqdm
import torch 
import torch.nn as nn
import torchvision
from torchsummary import summary
import torch.nn.functional as F
import torch.optim as optim

import import_ipynb
import EVA_Regularization as rg

def train(model, device, train_loader, optimizer, lambda_l1,criterion):
  model.train()
  pbar=tqdm(train_loader)
  correct = 0
  processed = 0
  train_losses=[]
  train_acc=[]


  for batch_idx, (data, target) in enumerate(pbar):
    data, target = data.to(device), target.to(device)

    optimizer.zero_grad()
    y_pred = model(data)
    loss = criterion(y_pred, target)

    # L1 Regularization

    #print('L1 los : ###',rg.get_l1_loss(model,lambda_l1))
    loss=loss+rg.get_l1_loss(model,lambda_l1)

    loss.backward()
    optimizer.step()

    processed+=len(data)

    pred = y_pred.argmax(dim=1, keepdim=True)
    correct+=pred.eq(target.data.view_as(pred)).sum().item()
    
    pbar.set_description('Train: Batch id: {} \tLoss: {:.6f}\t Accuracy:{:.3f}'.format(
        batch_idx, loss.item(),100*correct/processed))
    
    train_losses.append(loss.item())
    train_acc.append(100*correct/processed)

  return train_acc, train_losses

      #torch.save(network.state_dict(), '/results/model.pth')
      #torch.save(optimizer.state_dict(), '/results/optimizer.pth')
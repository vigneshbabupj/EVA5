import Visionaire
from Visionaire import data_albumentations
from Visionaire import data_loader #import CIFAR10_dataloader
from Visionaire import models
from Visionaire import EVA_models
from Visionaire.train import train
from Visionaire.test import test
from Visionaire.diagnostic import incorrect_Classification,plot_performace, class_accuracy
from Visionaire.gradcam import plot_grad_cam
from Visionaire.tuner import findLR

import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim.lr_scheduler import *
import matplotlib.pyplot as plt
import numpy as np
from torchsummary import summary


class trainer:
  def __init__(self,params):
    self.transform = params['Image_Augmentation']
    self.data = params['data']
    self.model_name = params['model']
    self.model_type = params['model_type']
    self.Batch_Size = params['Batch_Size']
    self.epochs =  params['epochs']
    self.criterion_name = params['criterion']
    self.L1_regularizer_lambda = params['L1_regularizer_lambda']
    self.L2_regularizer_lambda = params['L2_regularizer_lambda']
    self.optimizer_dict = params['optimizer']
    self.scheduler_dict = params['scheduler']
    
    # CUDA for PyTorch
    self.use_cuda = torch.cuda.is_available()
    self.device = torch.device("cuda" if self.use_cuda else "cpu")
    torch.backends.cudnn.benchmark = True

    self.seed=121

    torch.manual_seed(self.seed)

    print("Using Cuda : ", self.use_cuda)
    
    
    # Model
    if self.model_type == 'EVA':
      self.model_class = getattr(EVA_models, self.model_name)
      self.model = self.model_class().to(self.device)
    else:
      self.model_class = getattr(models, self.model_name)
      self.model = self.model_class().to(self.device)

    #Criterion

    self.criterion_class = getattr(nn,self.criterion_name)
    self.criterion = self.criterion_class()

    #optimizer
    self.optim_module = getattr(optim,self.optimizer_dict['name'])
    self.optimizer = self.optim_module(self.model.parameters(),self.optimizer_dict['lr'],self.optimizer_dict['momentum'],self.L2_regularizer_lambda)


  def load_data(self): 
    
    # Data loader
    print('Data Loader : ')
    self.data_loader = getattr(data_loader, self.data)
    self.train_loader,self.test_loader, self.classes = self.data_loader(self.Batch_Size,self.use_cuda,self.transform)
  
  def model_summary(self,input_size):
    model = self.model().to(device)
    print(summary(my_trainer.model, input_size=input_size))
    
  
  def find_lr(self):
  
    # Lr range test
    self.best_lr = findLR(self.model,self.train_loader,self.test_loader,self.criterion, self.optimizer,num_iteration = 100)
    print("Best lr :",self.best_lr)
    self.min_lr = self.best_lr/10

  def run(self,lr):
    
    self.best_lr = lr
    self.min_lr = self.best_lr/10
    
    #self.optimizer = self.optim_module(self.model.parameters(),self.min_lr,self.optimizer_dict['momentum'],self.L2_regularizer_lambda)
    
    #scheduler
    
    pct_start_val =  (((self.scheduler_dict['max_at_epoch']) * (len(self.train_loader))) / ((self.epochs) * (len(self.train_loader))) )
    
    self.scheduler_module = getattr(optim.lr_scheduler,self.scheduler_dict['name'])
    self.scheduler = self.scheduler_module(self.optimizer,max_lr=self.best_lr,total_steps = len(self.train_loader) *self.epochs , steps_per_epoch=len(self.train_loader), epochs=self.epochs,pct_start=pct_start_val,anneal_strategy='cos',div_factor=10 ,final_div_factor=10)
    
    #self.scheduler = self.scheduler_module (self.optimizer,base_lr =self.min_lr, max_lr=self.best_lr, step_size_up  = ((self.scheduler_dict['max_at_epoch']) * (len(self.train_loader)))
    #                                         ,step_size_down = ((self.epochs - (self.scheduler_dict['max_at_epoch'])) * (len(self.train_loader))) )

    
    self.train_losses = []
    self.test_losses = []
    self.train_accuracy = []
    self.test_accuracy = []
    self.lr_list=[]

    for epoch in range(self.epochs):
        print("\n EPOCH:", epoch)
        print("Learning Rate : ",self.optimizer.param_groups[0]['lr'])
        self.lr_list.append(self.optimizer.param_groups[0]['lr'])
        
        self.train_acc, self.train_loss = train(self.model, self.device, self.train_loader, self.optimizer,self.scheduler, self.L1_regularizer_lambda,self.criterion)
        self.train_losses.append(sum(self.train_loss)/len(self.train_loss))
        self.train_accuracy.append(sum(self.train_acc)/len(self.train_acc))
        
        self.test_acc, self.test_loss = test(self.model, self.device, self.test_loader, self.criterion)
        self.test_losses.append(self.test_loss)
        self.test_accuracy.append(self.test_acc)

        


  def plot_model_performance(self,save_plot=False,*save_dir):
    plot_performace(self.train_accuracy,self.test_accuracy,self.train_losses,self.test_losses,save_plot,save_dir)
  
  def plot_lr(self):
    plt.plot(self.lr_list)
    plt.title("Lr change in Epochs")
    plt.xlabel('Epochs')
    plt.ylabel('Learning Rate')
    plt.show()
    

  def grad_cam(self,save_plot=False,*save_dir):
    plot_grad_cam(self.model,self.classes,self.test_loader,self.device,25,save_plot,save_dir)


  def misclassified_images(self,save_plot=False,*save_dir):
    incorrect_Classification(self.model,self.classes,self.test_loader,self.device,save_plot,save_dir)


  def check_class_accuracy(self):
    class_accuracy(self.classes,self.model,self.test_loader,self.device)



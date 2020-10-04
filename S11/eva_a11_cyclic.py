# -*- coding: utf-8 -*-
"""EVA_A11_cyclic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t6KTvoc8xwPWDOmaXunQDyeC0FfbpRUg
"""

import numpy as np

Num_iterations = 1000
stepsize = 100

Max_lr = 10
Min_lr = 5

lr_list = []
for iteration in range(Num_iterations):
  cycle = np.floor(1+ (iteration / (2*stepsize)))
  x = abs(((iteration/stepsize) - 2*(cycle) + 1))
  lr_t = Min_lr + (Max_lr - Min_lr)*(1 - x)
  lr_list.append(lr_t)
  #print(lr_t)

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt

plt.axhline(Min_lr,label = 'LR min',color='r')
plt.axhline(Max_lr,label = 'LR max',color='r')
plt.plot(lr_list,label = 'LR')
plt.legend()
plt.ylim((1,15))
plt.show()


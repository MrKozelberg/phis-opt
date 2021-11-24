#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 11:18:18 2021

@author: mrk
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from PIL import Image
import numpy as np

col = ['tab:red', 'tab:green', 'tab:blue']

#%%%
nonius = np.asarray(Image.open("../data/1-0.jpg").convert("RGB"))
x = np.arange(np.shape(nonius)[0])
y = np.arange(np.shape(nonius)[1])
x_0 = 12

nonius_mean = [np.mean(nonius[x_0, i, :]) for i in y]


fig1, ax1 = plt.subplots(nrows=3, ncols=1, figsize=(6.5, 5))  # plotting
for i in range(3):
    ax1[i].plot(y, nonius[x_0, :, i], color=col[i])
    ax1[i].set_ylabel('Intensivity, ' + col[i][4:], color=col[i])
    ax1[i].set_xlim([0, max(y)])
    ax1[i].set_xticks(np.append(np.arange(0,max(y),50),max(y)))
    ax1[i].set_xticklabels(np.append(np.arange(0,max(y),50),max(y)))
    ax1[i].set_yticks(np.arange(0,210,50))
    ax1[i].grid()
ax1[2].set_xlabel('Pixel number')
plt.show()
fig1.savefig('../plots/1-0.jpg', dpi = 200)



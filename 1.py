#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 20:14:39 2021

@author: mrk
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

img = np.asarray(Image.open("1-1.jpg").convert("RGB"))
x = np.arange(np.shape(img)[0])
y = np.arange(np.shape(img)[1]);
y_0 = 126
col = ['tab:red', 'tab:green', 'tab:blue']

fig1, ax1 = plt.subplots(nrows=3, ncols=1, figsize=(9, 6))  # plotting
fig1.suptitle("Newton's rings",
              y=1.2,
              fontsize=30)
for i in range(3):
    ax1[i].plot(x, img[:, y_0, i], color=col[i])
    ax1[i].set_ylabel('Intensivity, ' + col[i][4:], color=col[i])
    ax1[i].set_xlim([0, max(x)])
    ax1[i].grid()
ax1[2].set_xlabel('Pixels')
plt.show()
fig1.savefig('newton_1.svg')

fig2, ax2 = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

# mean dark = 121 pxl
red_light = [10, 70.5, 95, 116.5]
red_dark = [0, 48, 82.5, 105.5]

green_light = [10.75, 66.25, 88.75, 106.25]
green_dark = [0, 48.5, 76, 106]

blue_light = [10.75, 59.25, 80]
blue_dark = [0, 41, 78.5]

red_light_x = np.arange(np.shape(red_light)[0])
green_light_x = np.arange(np.shape(green_light)[0])
blue_light_x = np.arange(np.shape(blue_light)[0])

red_light_lin = np.polyfit(red_light_x, red_light,1)
green_light_lin = np.polyfit(green_light_x, green_light,1)
blue_light_lin = np.polyfit(blue_light_x, blue_light,1)

ax2[0].set_title("Light")
ax2[0].scatter(red_light_x, red_light, color=col[0])
ax2[0].plot(red_light_x, red_light_lin, color=col[0], linestyle='dashed')
ax2[0].scatter(green_light_x, green_light, color=col[1])
ax2[0].plot(np.arange(green_light_x, green_light_lin, color=col[1], linestyle='dashed')
ax2[0].scatter(blue_light_x, blue_light, color=col[2])
ax2[0].plot(np.arange(blue_light_x, blue_light_lin, color=col[2], linestyle='dashed')

plt.show()

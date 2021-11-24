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

col = ['tab:red', 'tab:green', 'tab:blue']

#%%
# img = np.asarray(Image.open("../data/1-1.jpg").convert("RGB"))
# x = np.arange(np.shape(img)[0])
# y = np.arange(np.shape(img)[1]);
# y_0 = 126

# fig1, ax1 = plt.subplots(nrows=3, ncols=1, figsize=(9, 6))  # plotting
# for i in range(3):
#     ax1[i].plot(x, img[:, y_0, i], color=col[i])
#     ax1[i].set_ylabel('Intensivity, ' + col[i][4:], color=col[i])
#     ax1[i].set_xlim([0, max(x)])
#     ax1[i].grid()
# ax1[2].set_xlabel('Pixels')
# plt.show()
# fig1.savefig('../plots/newton_1.svg')

#%%
k=3e-3 # mm/pxl
fig = plt.figure(figsize = (10,16))
# mean dark = 121 pxl
# radii of rings, 0 - dark, 1 - light, let dr_m be 10 pxls

err = 10 * k

red = np.zeros((2,4))
red[0,:] = np.asarray([0, 48, 82.5, 105.5]) * k
red[1,:] = np.asarray([10, 70.5, 95, 116.5]) * k

green = np.zeros((2,4))
green[0,:] = np.asarray([0, 48.5, 76, 106]) * k
green[1,:] = np.asarray([10.75, 66.25, 88.75, 106.25]) * k

blue = np.zeros((2,3))
blue[0,:] = np.asarray([0, 41, 78.5]) * k
blue[1,:] = np.asarray([10.75, 59.25, 80]) * k

red_x = np.arange(red.shape[1])
green_x = np.arange(green.shape[1])
blue_x = np.arange(blue.shape[1])

red_reg = [np.polyfit(red_x, red[i,:]**2,1) for i in range(2)]
red_lin = [np.poly1d(red_reg[i]) for i in range(2)]
green_reg = [np.polyfit(green_x, green[i,:]**2,1) for i in range(2)]
green_lin = [np.poly1d(green_reg[i]) for i in range(2)]
blue_reg = [np.polyfit(blue_x, blue[i,:]**2,1) for i in range(2)]
blue_lin = [np.poly1d(blue_reg[i]) for i in range(2)]

ax2 = [[None for _ in range(2)] for _ in range(3)]

ax2[0][0] = fig.add_subplot(3,2,1)
ax2[0][0].set_xticks(np.arange(4))
ax2[0][0].set_xlabel('m, number of ring')
ax2[0][0].set_ylabel(r'$r_m^2$, ${mm}^2$')
ax2[0][0].set_title('Dark')
ax2[0][0].errorbar(red_x, red[0]**2, c = col[0], fmt = 'o',
                  yerr = 2 * red[0] * err)
ax2[0][0].plot(red_x, red_lin[0](red_x), c = col[0], linestyle = 'dashed',
               label = r'${:.2}\cdot m {:.2}$'.format(red_reg[0][0], red_reg[0][1]))
ax2[0][0].legend()
ax2[0][0].set_ylim([-0.01,0.16])

ax2[0][1] = fig.add_subplot(3,2,2)
ax2[0][1].set_xticks(np.arange(4))
ax2[0][1].set_xlabel('m, number of ring',y=5)
ax2[0][1].set_title('Light')
ax2[0][1].errorbar(red_x, red[1]**2, c = col[0], fmt = 'o',
                  yerr = 2 * red[1] * err)
ax2[0][1].plot(red_x, red_lin[1](red_x), c = col[0], linestyle = 'dashed',
               label = r'${:.2}\cdot m + {:.2}$'.format(red_reg[1][0], red_reg[1][1]))
ax2[0][1].legend()

ax2[1][0] = fig.add_subplot(3,2,3)
ax2[1][0].set_xticks(np.arange(4))
ax2[1][0].set_xlabel('m, number of ring')
ax2[1][0].set_ylabel(r'$r_m^2$, ${mm}^2$')
ax2[1][0].errorbar(green_x, green[0]**2, c = col[1], fmt = 'o',
                  yerr = 2 * green[0] * err)
ax2[1][0].plot(green_x, green_lin[0](green_x), c = col[1], linestyle = 'dashed',
               label = r'${:.2}\cdot m {:.2}$'.format(green_reg[0][0], green_reg[0][1]))
ax2[1][0].legend()
ax2[1][0].set_ylim([-0.01,0.16])

ax2[1][1] = fig.add_subplot(3,2,4)
ax2[1][1].set_xticks(np.arange(4))
ax2[1][1].set_xlabel('m, number of ring')
ax2[1][1].errorbar(green_x, green[1]**2, c = col[1], fmt = 'o',
                  yerr = 2 * green[1] * err)
ax2[1][1].plot(green_x, green_lin[1](green_x), c = col[1], linestyle = 'dashed',
               label = r'${:.2}\cdot m + {:.2}$'.format(blue_reg[1][0], blue_reg[1][1]))
ax2[1][1].legend()
ax2[1][1].set_ylim([-0.01,0.16])

ax2[2][0] = fig.add_subplot(3,2,5)
ax2[2][0].set_xticks(np.arange(4))
ax2[2][0].set_xlabel('m, number of ring')
ax2[2][0].set_ylabel(r'$r_m^2$, ${mm}^2$')
ax2[2][0].errorbar(blue_x, blue[0]**2, c = col[2], fmt = 'o',
                  yerr = 2 * blue[0] * err)
ax2[2][0].plot(np.arange(4), blue_lin[0](np.arange(4)), c = col[2], linestyle = 'dashed',
               label = r'${:.2}\cdot m {:.2}$'.format(blue_reg[0][0], blue_reg[0][1]))
ax2[2][0].legend()
ax2[2][0].set_ylim([-0.01,0.16])

ax2[2][1] = fig.add_subplot(3,2,6)
ax2[2][1].set_xticks(np.arange(4))
ax2[2][1].set_xlabel('m, number of ring')
ax2[2][1].errorbar(blue_x, blue[1]**2, c = col[2], fmt = 'o',
                  yerr = 2 * blue[1] * err)
ax2[2][1].plot(np.arange(4), blue_lin[1](np.arange(4)), c = col[2], linestyle = 'dashed',
               label = r'${:.2}\cdot m + {:.2}$'.format(blue_reg[1][0], blue_reg[1][1]))
ax2[2][1].legend()
ax2[2][1].set_ylim([-0.01,0.16])

fig.savefig('../plots/1-1.jpg', dpi = 200, bbox_inches = 'tight')



# ax2[0].scatter(green_x, green[0]**2, c = col[1], marker = 's', s = 40)
# ax2[0].scatter(blue_x, blue[0]**2, c = col[2], marker = 's', s = 30)


# ax2[0].plot(green_x, green_lin[0](green_x), c = col[1], linestyle = 'dashed')
# ax2[0].plot([0,1,2,3], blue_lin[0]([0,1,2,3]), c = col[2], linestyle = 'dashed')

# ax2[0].set
plt.show()

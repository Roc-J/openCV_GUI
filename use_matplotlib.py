#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('luxiaoyu.jpg', 0)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
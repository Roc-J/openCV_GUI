#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

import cv2

# Load the img
img = cv2.imread('luxiaoyu.jpg', -1)

cv2.namedWindow('路小雨', cv2.WINDOW_NORMAL)

cv2.imshow('路小雨', img)
cv2.imwrite('路小雨.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
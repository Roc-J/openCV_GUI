#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk
import cv2

img = cv2.imread('路小雨.png', -1)
cv2.imshow('路小雨', img)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('xiaoyu.jpg', img)
    cv2.destroyAllWindows()
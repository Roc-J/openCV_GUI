#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

import cv2
import numpy as np

# a black img
img = np.zeros((512, 512, 3), np.uint8)

# plot a line
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# plot a rect
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

# plot a circle
cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)

# draw ellipse
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 360, 255, -1)

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 255, 255))


# put text
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, 'Opencv Roc-J', (10, 500), font, 2, (200, 200, 200), 2, cv2.CV_AA)

cv2.imshow('Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
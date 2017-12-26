#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

import cv2

cap = cv2.VideoCapture('雪屋日落.avi')

while True:
    ret, frame = cap.read()

    if ret is True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imshow('雪屋日落', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
import cv2
import numpy as np
import matplotlib.pyplot as plt

IMAGE_H = 1024
IMAGE_W = 1280

src = np.float32([[0, IMAGE_H], [1207, IMAGE_H], [0, 0], [IMAGE_W, 0]])
dst = np.float32([[569, IMAGE_H], [711, IMAGE_H], [0, 0], [IMAGE_W, 0]])
M = cv2.getPerspectiveTransform(src, dst) # The transformation matrix
Minv = cv2.getPerspectiveTransform(dst, src) # Inverse transformation

img = cv2.imread('./test_image2.jpg') # Read the test img

if img is None: 
    raise ValueError('Something wrong with image.')
    
cv2.circle(img, (550, 420), 5, (0, 0, 255), -1)
cv2.circle(img, (670, 420), 5, (0, 0, 255), -1)
cv2.circle(img, (400, 560), 5, (0, 0, 255), -1)
cv2.circle(img, (790, 580), 5, (0, 0, 255), -1)

pts1 = np.float32([[550, 420], [670, 420], [400, 560], [790, 580]])
pts2 = np.float32([[550, 0], [670, 0], [550, 560], [670, 560]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)

result = cv2.warpPerspective(img, matrix, (IMAGE_W, IMAGE_H))
 
cv2.imshow('original',img) # Show results
cv2.imshow('transformed',result) # Show results
cv2.waitKey(0)
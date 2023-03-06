import cv2
import numpy as np

img = cv2.imread("matahari1.jpeg")

kernel_size = 5
kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size**2)
filtered_img = cv2.filter2D(img, -1, kernel)

cv2.imshow("Original Image", img)
cv2.imshow("Filtered Image", filtered_img)
cv2.waitKey(0)


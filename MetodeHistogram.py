import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('lena2.jpeg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('lena.jpeg', cv2.IMREAD_GRAYSCALE)

hist1, bins1 = np.histogram(img1.ravel(), 256, [0, 256])
hist2, bins2 = np.histogram(img2.ravel(), 256, [0, 256])

plt.subplot(221)
plt.imshow(img1, cmap='gray')
plt.title('Original Image 1')

plt.subplot(222)
plt.imshow(img2, cmap='gray')
plt.title('Original Image 2')

plt.subplot(223)
plt.hist(img1.ravel(), 256, [0, 256])
plt.title('Histogram Image 1')

plt.subplot(224)
plt.hist(img2.ravel(), 256, [0, 256])
plt.title('Histogram Image 2')

plt.show()
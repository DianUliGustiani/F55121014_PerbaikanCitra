import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('lena2.jpeg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('lena.jpeg', cv2.IMREAD_GRAYSCALE)

eq_img1 = cv2.equalizeHist(img1)
eq_img2 = cv2.equalizeHist(img2)

plt.subplot(221)
plt.imshow(img1, cmap='gray')
plt.title('Original Image 1')

plt.subplot(222)
plt.imshow(eq_img1, cmap='gray')
plt.title('Equalized Image 1')

plt.subplot(223)
plt.imshow(img2, cmap='gray')
plt.title('Original Image 2')

plt.subplot(224)
plt.imshow(eq_img2, cmap='gray')
plt.title('Equalized Image 2')

plt.show()
import cv2

img1 = cv2.imread('matahari1.jpeg')
img1 = cv2.resize(img1, (359, 300))
img2 = cv2.imread('matahari2.jpeg')
img2 = cv2.resize(img2,(359, 300))

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

diff = cv2.subtract(gray1, gray2)

cv2.imshow('img1', img1)
cv2.imshow('img2',img2)
cv2.imshow('Difference', diff)
cv2.waitKey(0)
cv2.destroyAllWindows()
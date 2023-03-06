import cv2

img1 = cv2.imread('matahari1.jpeg')
img1 = cv2.resize(img1, (600, 600))
img2 = cv2.imread('matahari2.jpeg')
img2 = cv2.resize(img2, (600, 600))

diff_img = cv2.absdiff(img1, img2)

cv2.imshow('Difference Image', diff_img)
cv2.waitKey(0)
cv2.destroyAllWindows
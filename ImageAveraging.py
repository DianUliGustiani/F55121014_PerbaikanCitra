import cv2

img1 = cv2.imread('matahari1.jpeg')
img2 = cv2.imread('matahari2.jpeg')

img1 = cv2.resize(img1, (640, 600))
img2 = cv2.resize(img2, (640, 600))

result = cv2.addWeighted(img1,0.5, img2, 0.5, 0)

cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
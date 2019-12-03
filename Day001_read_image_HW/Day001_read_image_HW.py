#load cv2
from cv2 import cv2

#read picture, and resize it.
img = cv2.imread('point out.jpg', cv2.IMREAD_COLOR)
img_color = cv2.resize(img, (1600, 900))

#show the colorful picture in window, close it,  and write in file
cv2.imshow('full_size', img)
cv2.imshow('small size', img_color)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite('small_color.jpg', img_color)


#read the picture in gray
img = cv2.imread('point out.jpg', cv2.IMREAD_GRAYSCALE)
img_gray = cv2.resize(img, (1600,900))

#show the grayful picture in window, close it,  and write in file
cv2.imshow('Gray', img)
cv2.imshow('gray_small', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows
cv2.imwrite('small_gray.jpg', img_gray)
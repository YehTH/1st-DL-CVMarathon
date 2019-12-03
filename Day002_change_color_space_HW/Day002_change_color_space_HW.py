from cv2 import cv2

img = cv2.imread('point out.jpg', cv2.IMREAD_COLOR)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
img_lab2 = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
img_l2b = cv2.cvtColor(img, cv2.COLOR_LAB2BGR)

cv2.imshow('BGR2HSV',img_hsv)
cv2.imshow('BGR2HSV',img_hls)
cv2.imshow('BGR2HSV',img_lab)
cv2.imshow('BGR2HSV',img_lab2)
cv2.imshow('BGR2HSV',img_l2b)

cv2.imwrite('img_hsv.jpg', img_hsv)
cv2.imwrite('img_hls.jpg', img_hls)
cv2.imwrite('img_lab.jpg', img_lab)
cv2.imwrite('img_lab2.jpg', img_lab2)
cv2.imwrite('img_l2b.jpg', img_l2b)

cv2.waitKey(0)
cv2.destroyAllWindows
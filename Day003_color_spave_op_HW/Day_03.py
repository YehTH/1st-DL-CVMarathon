from cv2 import cv2
import numpy as np


img_ = cv2.imread('point out.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img_, (1600,900))


#Histogram Equalization for RGB
# from cv2 import equalizeHist
img_rgb = cv2.equalizeHist(img)

#Histogram Equalization for HSL
# img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
# cv2.equalizeHist(img_hsv)

# cv2.imshow('img_hsv', img_hsv)
# cv2.waitKey(0)
cv2.imshow('img', img)
cv2.imshow('img_rgb', img_rgb)
cv2.waitKey(0)
cv2.destoryAllWindows()

# cv2.imwrite('point out_hsv.jpg', img_hsv)
cv2.imwrite('point out_rgb.jpg', img_rgb)


# using function to show and write
img_function_1 = cv2.convertScaleAbs(img,2.0,0)
img_function_2 = cv2.convertScaleAbs(img,1.0,50)

cv2.imshow('window', img_function_1)
cv2.imshow('window', img_function_2)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('point out_function_1.jpg', img_function_1)
cv2.imwrite('point out_function_2.jpg', img_function_2)


# using loop
# from cv2 import equalizeHist

# alpha = 0.1
# beta = 45

# for b in range(img.shape[0]):
#     for g in range(img.shape[1]):
#         for r in range(img.shape[2]):
#             img[b, g, r] = np.clip(alpha * img[b, g, r]+beta, 0,255)

# cv2.imshow('loop', img)
# cv2.waitKey(0)
# cv2.destoryAllwindows()

# cv2.imwrite('point out_loop.jpg',img)
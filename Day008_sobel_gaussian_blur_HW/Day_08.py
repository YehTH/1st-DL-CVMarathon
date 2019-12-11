#load package and photo

from cv2 import cv2 as cv
import numpy as np

img = cv.imread('point out.jpg', cv.IMREAD_COLOR)
img_resize_color = cv.resize(img, (1600,900))
#image blur
img_blur = cv.GaussianBlur(img_resize_color, (11,11), 0)



img_gray = cv.imread('point out.jpg', cv.IMREAD_GRAYSCALE)
img_resize_gray = cv.resize(img_gray, (1600, 800))

# sobel the image, "CV_8U", diff = 1, write it.
img_x = cv.Sobel(img_resize_gray, cv.CV_8U, dx = 1, dy = 0, ksize = 5)
img_y = cv.Sobel(img_resize_gray, cv.CV_8U, dx = 0, dy = 1, ksize = 5)
img_x = cv.convertScaleAbs(img_x)
img_y = cv.convertScaleAbs(img_y)
img_combine = cv.addWeighted(img_x, 0.5, img_y, 0.5, 0 )
cv.imwrite('point out_sobel_CV8U.jpg', img_combine)

# sobel the image, diff = 1, write it.
img_x = cv.Sobel(img_resize_gray, cv.CV_16S, dx = 1, dy = 0, ksize = 5)
img_y = cv.Sobel(img_resize_gray, cv.CV_16S, dx = 0, dy = 1, ksize = 5)
img_x = cv.convertScaleAbs(img_x)
img_y = cv.convertScaleAbs(img_y)
img_combine = cv.addWeighted(img_x, 0.5, img_y, 0.5, 0 )
cv.imwrite('point out_sobel_diff01.jpg', img_combine)

# sobel the image, diff = 2, write it.
img_x = cv.Sobel(img_resize_gray, cv.CV_16S, dx = 2, dy = 0, ksize = 5)
img_y = cv.Sobel(img_resize_gray, cv.CV_16S, dx = 0, dy = 2, ksize = 5)

img_x = cv.convertScaleAbs(img_x)
img_y = cv.convertScaleAbs(img_y)
img_combine = cv.addWeighted(img_x, 0.5, img_y, 0.5, 0 )
cv.imwrite('point out_sobel_diff02.jpg', img_combine)

# show and write the photo
cv.imwrite('point out_blur.jpg', img_blur)
cv.imwrite('point out_sobel.jpg', img_combine)

cv.imshow('win',img_combine)
cv.waitKey(0)
cv.destroyAllWindows()



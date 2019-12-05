from cv2 import cv2

img = cv2.imread('point out.jpg', cv2.IMREAD_COLOR)
img_flip = cv2.resize(img, (800, 450))

#Vertical and herizontal flip the photo
cv2.imshow('vertical flip', img_flip[::-1, :, :])
cv2.waitKey(500)
cv2.imshow('Herizontal flip', img_flip[:, ::-1, :])
cv2.waitKey(500)
cv2.destroyAllWindows()



#Resize the photo
print (img.shape)

#you can enter a percitage number to resise the photo :)
pert = int(input('Please enter a percitage number to resise the photo: '))

# width = int(img.shape[1] * pert / 100)
width = int(img.shape[1] * pert / 100)
heigth = int(img.shape[0] * pert / 100)

img_nearest = cv2.resize(img, (width, heigth), cv2.INTER_NEAREST)
img_cubic = cv2.resize(img, (width, heigth), cv2.INTER_CUBIC)
cv2.imwrite('point out_nearest.jpg', img_nearest)
cv2.imwrite('point out_cubic.jpg', img_cubic)

print(img_nearest.shape, ' vs. ', img_cubic.shape)

#Affine function
import numpy as np

row, col, chn = img_cubic.shape
print (img_cubic.shape, row, col, chn)

row_1 = int(row/4)
col_1 = int(col/4)
print(row_1, col_1)
cv2.circle(img_cubic, (col_1, row_1), 3, (0, 0, 255),-1)    #the col & row value should exchange in _.shape
cv2.circle(img_cubic, (col_1*3, row_1), 3, (0, 0, 255))
cv2.circle(img_cubic, (col_1, row_1*3), 3, (0, 0, 0),-1)

point_1 = np.float32([[col_1, row_1],[col_1*3, row_1], [col_1, row_1*3]])
point_2 = np.float32([[col_1+100, row_1],[col_1*3, row_1], [col_1-100, row_1*3]])

matrix = cv2.getAffineTransform(point_1, point_2)
result = cv2.warpAffine(img_cubic, matrix, (row, col))
cv2.imwrite('point out_affine.jpg',result)

cv2.imshow('Affine', img_cubic)
cv2.waitKey(0)
cv2.imshow('Change', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

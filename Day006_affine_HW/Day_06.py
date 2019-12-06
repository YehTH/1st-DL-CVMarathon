from cv2 import cv2

#read the file
img = cv2.imread('point out.jpg')
col, row, chn = img.shape
col_1 = int(col/4)
row_1 = int(row/4)

#draw the circle on the photo
cv2.circle(img, (row_1, col_1), 20, (0, 0, 255), -1)
cv2.circle(img, (row_1*3, col_1), 20, (0, 0, 255), -1)
cv2.circle(img, (row_1, col_1*3), 20, (0, 0, 255), -1)

#rotate the photo, get the transtation matrix
rotate_matrix = cv2.getRotationMatrix2D((row_1*2, col_1*2), -45, 0.5)
img_affine = cv2.warpAffine(img, rotate_matrix, (1000, -500))

#draw the circle on the photo again
cv2.circle(img_affine, (row_1, col_1), 10, (255, 255, 255), -1)
cv2.circle(img_affine, (row_1*3, col_1), 10, (255, 255, 255), -1)
cv2.circle(img_affine, (row_1, col_1*3), 10, (255, 255, 255), -1)


#show all photo
# cv2.imshow('win',img_affine)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
cv2.imwrite('point out_change.jpg', img_affine)
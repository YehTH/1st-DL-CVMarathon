from cv2 import cv2

#read the photo, and get the photo info.
img = cv2.imread('point out.jpg', cv2.IMREAD_GRAYSCALE)
col, row = img.shape
print(row, col)
row_1 = int(row/4) 
col_1 = int(col*0.25)

#equalizeHist the photo
img_gray = cv2.equalizeHist(img)

#Herizontle flip it. Those is no color channel
img_flip = cv2.flip(img_gray, 1)

#draw a retangle on the photo
img_retangle = cv2.rectangle(img_flip, (row_1, col_1), (row_1 *3, col_1 *3), (0,0,255), -1)

#down-size it.
img_resize = cv2.resize(img_retangle,(row, col))

#write the result
cv2.imwrite('img_result.jpg', img_resize)
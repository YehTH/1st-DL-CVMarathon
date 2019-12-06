from cv2 import cv2

#read the photo


#Vertical and herizontal flip the photo


#Resize the photo


#you can enter a percitage number to resise the photo :)


# width = int(img.shape[1] * pert / 100)


#Affine function
	#I'm not sure what is the function np.float32, and using.
45.
46.

	#the sit of _.shape & cv2.circle() is in opp site. 
35.
41.
42.
43.

	#make sure the difference between getAffineTranslation() and  warpAffine()
48.
49.



Reference: 
https://pysource.com/2018/02/15/affine-transformation-opencv-3-4-with-python-3-tutorial-14/
https://docs.opencv.org/2.4/modules/imgproc/doc/geometric_transformations.html#void%20warpAffine(InputArray%20src,%20OutputArray%20dst,%20InputArray%20M,%20Size%20dsize,%20int%20flags,%20int%20borderMode,%20const%20Scalar&%20borderValue)
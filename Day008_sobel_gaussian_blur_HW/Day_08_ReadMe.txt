#load package and photo


#image blur

# sobel the image, "CV_8U", diff = 1, write it.
    #the CV_8U vs. CV_16S, this two are different.

# sobel the image, diff = 1, write it.
    #the impact of blur are according to the kenner array size & sigmaX.
    #ksize is the array size which impacts the photo.

# sobel the image, diff = 2, write it.


# show and write the photo







Reference:
https://docs.opencv.org/2.4/modules/core/doc/basic_structures.html
    #CV_8U - 8-bit unsigned integers ( 0..255 )
    #CV_8S - 8-bit signed integers ( -128..127 )
    #CV_16U - 16-bit unsigned integers ( 0..65535 )
    #CV_16S - 16-bit signed integers ( -32768..32767 )
    #CV_32S - 32-bit signed integers ( -2147483648..2147483647 )
    #CV_32F - 32-bit floating-point numbers ( -FLT_MAX..FLT_MAX, INF, NAN )
    #CV_64F - 64-bit floating-point numbers ( -DBL_MAX..DBL_MAX, INF, NAN )
    
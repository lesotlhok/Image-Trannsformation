
import numpy as np
import cv2
import matplotlib.pyplot as plt

# read the input image
img = cv2.imread("images/City/city1.jpeg")
# convert from BGR to RGB so we can plot using matplotlib
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# disable x & y axis
plt.axis('off')
# show the image
plt.imshow(img)
plt.show()
# get the image shape
rows, cols, dim = img.shape
# transformation matrix for Shearing
# shearing applied to x-axis
M = np.float32([[1, 0.5, 0],
             	[0, 1  , 0],
            	[0, 0  , 1]])
# shearing applied to y-axis
# M = np.float32([[1,   0, 0],
#             	  [0.5, 1, 0],
#             	  [0,   0, 1]])
# apply a perspective transformation to the image
sheared_img = cv2.warpPerspective(img,M,(int(cols*1.5),int(rows*1.5)))
# disable x & y axis
plt.axis('off')
# show the resulting image
plt.imshow(sheared_img)
plt.show()
# save the resulting image to disk
plt.imsave("city1_sheared.jpg", sheared_img)


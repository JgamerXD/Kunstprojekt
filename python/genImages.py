import numpy as np
import cv2
import random

#Generates single color images in different sizes for testing

#sizes
widths = [100,200,400,500]
heights = [400,800,1200]


#number of images per size
num = 5
#diversity in %
div = 0.1

for w in widths:
	for h in heights:
		for i in range(num):
			color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
			ww = int(w * random.uniform(1-div, 1+div))
			hh = int(h * random.uniform(1-div, 1+div))
			im = np.zeros((hh,ww,3),dtype=np.uint8)
			im[:,:,:] = color
			cv2.imwrite(".\images\{}x{}_{}.png".format(w,h,i),im)

	
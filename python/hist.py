import matplotlib.pyplot as plt
import numpy as np
import cv2
import argparse
import json
import io


parser = argparse.ArgumentParser(description='Generates histograms from a json file containing the average colors of images')
parser.add_argument('input', metavar='I', nargs=1,help='Input json file')
args = parser.parse_args()

jf = io.open(args.input[0])
imgs = json.load(jf)
jf.close()
    
means = np.expand_dims(np.array([i["col"] for i in imgs["images"]],dtype=np.uint8),1)
#convert to HSV for better display
means = cv2.cvtColor(cv2.cvtColor(means,cv2.COLOR_LAB2BGR),cv2.COLOR_BGR2HSV).astype(np.uint16)
means[:,:,0] *= 2
print("means:",means.shape,means.dtype,max(means[:,:,0]))

hist1 = cv2.calcHist([np.array(means)], [0], None, [360], [0, 360])
hist2 = cv2.calcHist([np.array(means)], [1,0], None, [256, 360], [0, 256, 0, 360])

plt.figure()
plt.plot(range(360),hist1,"b-")
plt.figure()
plt.imshow(hist2,interpolation = 'nearest',origin='lower',cmap='bone')
plt.show()
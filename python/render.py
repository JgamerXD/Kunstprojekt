from math import *

import numpy as np
import argparse
import json
import io
import cv2
import time


#define arguments
parser = argparse.ArgumentParser(description='Renders sorted images')
parser.add_argument('images', metavar='I', nargs=1,help='json with images')
parser.add_argument('sorting', metavar='S', nargs=1,help='json with sorting data')
parser.add_argument('out', metavar='O', nargs=1,help='output image')

args = parser.parse_args()

#the time the program was started
startTime = time.time()
#prints log messages in the format [time since start]:  [message]
def logtime(msg):
    print("{:.3f}:\t {}".format(time.time() - startTime,msg))

    
logtime("Loading files")
#load json file with information about the grid and images
ijf = io.open(args.images[0])
imgs = json.load(ijf)
ijf.close()

#load json file containing the sorted image positions
sjf = io.open(args.sorting[0])
sort = json.load(sjf)
sjf.close()
    
grid = imgs["grid"]

images_temp = imgs["images"]


logtime("Setting up vars")
    
images = {}

for i in images_temp:
    images[str(i["id"])] = i

del images_temp

#print(images)

cellW = grid.get("cellWidth")
cellH = grid.get("cellHeight")


width = grid.get("gridWidth") * cellW
height = grid.get("gridHeight") * cellH


#sorted images
output = np.zeros((width,height,3),dtype=np.uint8)
#average colors of sorted images
meanOut = np.zeros((width,height,3),dtype=np.uint8)

logtime("Drawing")

for entry in sort:
    id = str(entry["id"])

    x = entry["x"] * cellW
    y = entry["y"] * cellH
    w = images[id]["w"] * cellW
    h = images[id]["h"] * cellH
    
    
    image = cv2.imread(images[id]["file"])
    iw = image.shape[0]
    ih = image.shape[1]
    wr = int((iw - w)/2)
    hr = int((ih - h)/2)

    output[x:x+w,y:y+h,:] = image[wr:wr+w,hr:hr+h,:]
    
    meanOut[x:x+w,y:y+h,:] = images[id]["col"]
    

#cv2.imshow("output",meanOut)
#cv2.waitKey(0)

#convert average colors from Lab to BGR
meanOut = cv2.cvtColor(meanOut,cv2.COLOR_LAB2BGR)


logtime("Writing to disk")
cv2.imwrite(args.out[0],output)
cv2.imwrite("mean_" + args.out[0],meanOut)
logtime("Done!")
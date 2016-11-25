from os import listdir
from os.path import isfile, join
from math import *

import numpy as np
import matplotlib.pyplot as plt
import argparse
import json
import io
import cv2
import time


#define arguments
parser = argparse.ArgumentParser(description='Analyzes images for sorting')
parser.add_argument('out', metavar='O', nargs=1,help='output json')
parser.add_argument('dirs', metavar='D', nargs='+',help='directory(s) with images')

args = parser.parse_args()


#the time the program was started
startTime = time.time()
#prints log messages in the format [time since start]:  [message]
def logtime(msg):
    print("{:.3f}:\t {}".format(time.time() - startTime,msg))


logtime("Load images")
    
#all files in target directories
files = []

#find files in directories
for d in args.dirs:
	files = files + [join(d,f) for f in listdir(d) if isfile(join(d, f))]

#load an image from each file
images = [cv2.imread(f) for f in files]
#discard invalid images and corresponding files
imfi = np.array([[i,f] for i,f in zip(images,files) if not i is None])
files = imfi[:,1]

#convert images to the L*a*b color space for easier sorting
images = np.array([cv2.cvtColor(i,cv2.COLOR_BGR2LAB) for i in imfi[:,0]])


del imfi


#print number of images
print("Loaded {} images.".format(len(images)))



logtime("Get average colors")


means = [[int(j) for j in i.mean(0).mean(0)] for i in images]


logtime("Calculate optimal cell size")


#image sizes
sizes = np.array([i.shape for i in images],dtype=np.int)

del images

#minimal sizes
minw = np.min(sizes[:,0])
minh = np.min(sizes[:,1])


"""
Bedingungen an Rastergröße
- Kleiner als kleinstes Bild
- möglichst nah an anderen
"""

#height
hscorestmp = []
for i in range(2,minh+1):
    steps = set()
    diff = 0
    for h in sizes[:,1]:
        steps.add(int(h/i))
        diff += h % i
    diff /= sizes.shape[1]
    score = diff * len(steps) ** 3 - i
    hscorestmp.append((i,score,diff,len(steps)))
    
hscores = np.array(hscorestmp)
del hscorestmp

#width
wscorestmp = []
for i in range(2,minw+1):
    steps = set()
    diff = 0
    for w in sizes[:,0]:
        steps.add(int(w/i))
        diff += w % i
    diff /= sizes.shape[1]
    score = diff * len(steps) ** 3 -i
    wscorestmp.append((i,score,diff,len(steps)))
    
wscores = np.array(wscorestmp)
del wscorestmp






logtime("Show results")

plt.figure()
plt.plot(hscores[:,0],(hscores[:,1]/max(hscores[:,1])),'r-',
                        (hscores[:,2]/max(hscores[:,2])),'b-',
                        (hscores[:,3]/max(hscores[:,3])),'g-')
                        
plt.axvline(np.argmin(hscores[:,1]))                     

plt.figure()

plt.plot(wscores[:,0],(wscores[:,1]/max(wscores[:,1])),'r-',
                        (wscores[:,2]/max(wscores[:,2])),'b-',
                        (wscores[:,3]/max(wscores[:,3])),'g-')
                        
plt.axvline(np.argmin(wscores[:,1]))                     
plt.show()


logtime("Calculate grid size")


cw = np.argmin(wscores[:,1])

ch =  np.argmin(hscores[:,1])




#image sizes in grid
gss = []
for s in sizes:
    gss.append((int(s[0]/cw),int(s[1]/ch)))
gridsizes = np.array(gss)
del gss

#calculate area covered by images
ass = np.multiply(gridsizes[:,0],gridsizes[:,1])
area = np.sum(ass)

#Seitenverhältnisse der Bilder  w/h
aspects = gridsizes[:,0]/gridsizes[:,1]  

aspect = aspects.mean()
del aspects

print(aspect)

gw = int(sqrt(area / aspect + 1))
gh = int(area / gw)

gw += int(minh/ch)
gh += int(minw/cw)



logtime("Compiling data")

grid = {"cellHeight":int(ch),"cellWidth":int(cw),"gridHeight":int(gh),"gridWidth":int(gw)}




imageData=[]
id = 0
for mean, gridsize, file in zip(means,gridsizes,files):
    imageData.append({"id":id,"file":file,"w": int(gridsize[0]), "h": int(gridsize[1]), "col":mean})
    id = id+1

#print(grid,imageData)
logtime("Writing to disk")
    
out = io.open(args.out[0],mode='wt')
json.dump({"grid":grid, "images":imageData},out)
out.close()



#print([f[0] for f in images])
#print(images)
from os import listdir
from os.path import isfile, join
#from collections import dict
#from sets import Set
import matplotlib.pyplot as plt

import argparse
import json
import io
from math import *

import cv2
import numpy as np

parser = argparse.ArgumentParser(description='Analyzes images for sorting')
parser.add_argument('dirs', metavar='D', nargs='+',help='directory(s) with images')

args = parser.parse_args()




files = []

#Dateien in Ordnern finden
for d in args.dirs:
	files = files + [join(d,f) for f in listdir(d) if isfile(join(d, f))]

images = [cv2.imread(f) for f in files]
#Nur geladene Bilder behalten
imfi = np.array([(i,f) for i,f in zip(images,files) if not i == None])
images = np.array([cv2.cvtColor(i,cv2.COLOR_BGR2HSV) for i in imfi[:,0]])
#cv2.imshow("debug",images[0])
#cv2.waitKey(0)
files = imfi[:,1]
del imfi


#Breite und Hoehe aller Bilder 
sizes = np.array([i.shape for i in images],dtype=np.int)

print(images.shape)

means = [(i[:,:,0].mean(),i[:,:,1].mean(),i[:,:,2].mean()) for i in images]
#print(means)
del images


minw = np.min(sizes[:,0])
minh = np.min(sizes[:,1])

"""
- Kleiner als kleinstes Bild
- möglichst nah an anderen
"""

hscorestmp = []


for i in range(2,minh+1):
    steps = set()
    diff = 0
    for h in sizes[:,1]:
        steps.add(int(h/i))
        diff += h % i
    diff /= sizes.shape[1]
    score = i + diff * len(steps) ** 3
    hscorestmp.append((i,score,diff,len(steps)))
    
hscores = np.array(hscorestmp)
del hscorestmp

'''
plt.plot(hscores[:,0],(hscores[:,1]/max(hscores[:,1])),'r-',
                        (hscores[:,2]/max(hscores[:,2])),'b-',
                        (hscores[:,3]/max(hscores[:,3])),'g-')
                        
plt.axvline(np.argmin(hscores[:,1]))                     
plt.show()'''

wscorestmp = []
for i in range(2,minw+1):
    steps = set()
    diff = 0
    for w in sizes[:,0]:
        steps.add(int(w/i))
        diff += w % i
    diff /= sizes.shape[1]
    score = i + diff * len(steps) ** 3
    wscorestmp.append((i,score,diff,len(steps)))
    
wscores = np.array(wscorestmp)
del wscorestmp


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





cw = np.argmin(wscores[:,1])

ch =  np.argmin(hscores[:,1])





gss = []

for s in sizes:
    gss.append((int(s[0]/cw),int(s[1]/ch)))
gridsizes = np.array(gss)
del gss

ass = np.multiply(gridsizes[:,0],gridsizes[:,1])

area = np.sum(ass)

#Seitenverhaeltnisse der Bilder  w/h
aspects = sizes[:,0]/sizes[:,1]  

aspect = aspects.mean()
del aspects

print(aspect)

gh = int(sqrt(area / aspect + 1))
gw = int(area / gh)

gh += int(minh/ch)
gw += int(minw/cw)



grid = {"cellHeight":int(ch),"cellWidth":int(cw),"gridHeight":int(gh),"gridWidth":int(gw)}


imageData=[]
for mean, gridsize, file in zip(means,gridsizes,files):
    imageData.append({"file":file,"w": int(gridsize[0]), "h": int(gridsize[1]), "col":[int(i) for i in mean]})

#print(grid,imageData)
    
out = io.open("./test.json",mode='wt')
json.dump({"grid":grid, "images":imageData},out)
out.close()



#print([f[0] for f in images])
#print(images)
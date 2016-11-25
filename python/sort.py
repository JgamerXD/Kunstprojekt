from os import listdir
from os.path import isfile, join
from json import JSONEncoder
from collections import namedtuple
from math import *

import numpy as np
import io
import time
import argparse
import json
import cv2




	
#define arguments
parser = argparse.ArgumentParser(description='Sorts analyzed images, optionally using a target image')
parser.add_argument('input', metavar='I', nargs=1,help='Input json file')
parser.add_argument('output', metavar='O', nargs=1,help='Output json file')
parser.add_argument('target', metavar='T', nargs='?',help='Target image')
parser.add_argument('-d','--debug', action='store_true',help='Show debug info')


args = parser.parse_args()

#Scores with position and score
Score = namedtuple('Score',['x','y','score'])

#image with id, size, color, scores and position (after sorting)
class ImgDat:
    px = 0
    py = 0
    scores = []
    
    def __init__(self,id,w,h,col):
        self.id = id
        self.w = w
        self.h = h
        self.col = col

#allows the ImgDat class to be encoded to json
class ImgDatJSONEncoder(JSONEncoder):
    def default(self,obj):
        if isinstance(obj,ImgDat):
            return dict(id=str(obj.id),x=int(obj.px),y=int(obj.py))
        
        return json.JSONEncoder.default(self,obj)
  




#the time the program was started
startTime = time.time()
#prints log messages in the format [time since start]:  [message]
def logtime(msg):
    print("{:.3f}:\t {}".format(time.time() - startTime,msg))

    
    
    
    
    
#all images  
images = []


logtime("Reading input...")
#load json file with information about the grid and images
jf = io.open(args.input[0])
imgs = json.load(jf)
jf.close()
    
#information about the grid
gridWidth = imgs["grid"].get("gridWidth")
gridHeight = imgs["grid"].get("gridHeight")

    
#get ImgDat objects from the json file
for i in imgs["images"]: 
    imgdat = ImgDat(i.get('id'),i.get('w'),i.get('h'),i.get('col'))
    images.append(imgdat)
	

#the number of images being sorted
numImages = len(images)







#generate default color lookup if no / an invalid target image was specified
def defaultLookup():
    global colorLookup
    #calculate optimal colors
    colorLookup = np.zeros((gridWidth,gridHeight,3),dtype=np.uint8)
    for i in range(gridWidth):
        for j in range(gridHeight):
            #h[0,179] s[0,255] v[0,255]
            c = (int((float(i)/gridWidth+float(j)/gridHeight)/2.0*179),255,255)
            #print(i,j,c)
            colorLookup[i,j,:] = c

    colorLookup = cv2.cvtColor(colorLookup,cv2.COLOR_HSV2BGR)       
    
    cv2.imshow("lookup.png",cv2.resize(colorLookup,(0,0),fx = 10, fy = 10, interpolation = cv2.INTER_NEAREST))
    cv2.waitKey(10000)
    #cv2.destroyWindow("lookup.png")


    colorLookup = cv2.cvtColor(colorLookup,cv2.COLOR_BGR2LAB)
    cv2.destroyWindow("lookup.png")
    cv2.imwrite("lookup.png",cv2.cvtColor(colorLookup,cv2.COLOR_LAB2BGR))

#generate color lookup from target image
def lookupFromImage(img):
    global colorLookup
    image = cv2.imread(img)
    #print(img, image)
    if image is None:
        defaultLookup()
        return
    print("Using image as target")
    colorLookup =  cv2.cvtColor(cv2.resize(image,(gridHeight,gridWidth)),cv2.COLOR_BGR2LAB)
    #print(colorLookup.shape)



        
            
def sortImages(images,w,h):
    #representation of final image by image ids
    table = np.zeros((w,h),dtype=np.int)
    
    #sort images by size
    images = sorted(images,key = lambda i: i.w*i.h,reverse=True)
    errors = 0
    for img in images:
        current = img
        placed = False
        #for every score; good -> bad
        for sc in current.scores:
            #check if spot is free
            if np.amax(table[sc.x:sc.x+current.w,sc.y:sc.y+current.h]) <= 0:
                table[sc.x:sc.x+current.w,sc.y:sc.y+current.h] = images.index(current)
                current.px = sc.x
                current.py = sc.y
                placed = True
                break
           
        if not placed:
            #print an error message if image did not fit anywhere
            print("{} could not be placed ({}x{})".format(current.id,current.w,current.h))
            errors = errors + 1
    print("could not place {} images".format(errors))
    return table       
            

#write the output json file with the images' ids and positions 
def output(images):
    outfile=args.output[0]
    if not outfile.endswith('.json'):
        outfile += '.json'
    t = io.open(outfile, mode='wt')
    json.dump(images,fp=t,cls=ImgDatJSONEncoder)
    t.close()

#normalizes an array to ]0;1[
def normalized(a):
    a = a - np.min(a)
    a = a / np.max(a)
    return a
  


#calculate a single score for image at position
def calcScore(image,x,y):
    #get color of target region in lookup table
    tc = colorLookup[x:x+image.w,y:y+image.h,:].mean(0).mean(0)
    
    #calculate euclidean distance between image and target color
    # --> score
    sc = sqrt(np.sum((tc - image.col) ** 2))
    
    return Score(x,y,sc)
    
#calculate scores as the euclidean distance between the color of the image and the target color   
def calcScores(images,sx,sy):
    #for every image
    for i in images:
        scores = []
        #for every possible position of image
        for x in range(0,sx-i.w+1):
            for y in range(0,sy-i.h+1):
                scores.append(calcScore(i,x,y))
        
        
        #show distribution of scores if debugging is enabled
        if args.debug:
            
            npscores = np.array([s.score for s in scores]).reshape(sx-i.w+1,sy-i.h+1)
            npscores = normalized(npscores) * 255
            npscores = npscores.astype(np.uint8)

            cv2.imshow("score", cv2.resize(cv2.applyColorMap(npscores,cv2.COLORMAP_JET),(0,0),fx = 10, fy = 10, interpolation = cv2.INTER_NEAREST))
            cv2.waitKey(1)
        
        #sort scores by value (lower is better)
        i.scores = sorted(scores,key=lambda s: s.score)       

    
#generate lookup
if not args.target is None:
    lookupFromImage(args.target)
else:
    defaultLookup()
    
logtime("Calculating scores...")

calcScores(images,gridWidth,gridHeight)
logtime("Sorting...")

sortImages(images,gridWidth,gridHeight)
#for i in images:
#   print(i.id,i.px,i.py)

logtime("Generating output...")
output(images)

logtime("Done!")
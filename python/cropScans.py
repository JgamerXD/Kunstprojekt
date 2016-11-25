from os import listdir, open, write, close
from os.path import *

import io
import cv2
import numpy as np
import argparse



parser = argparse.ArgumentParser(description='crops')

parser.add_argument('out', metavar='O', nargs=1,help='output directory')
parser.add_argument('dirs', metavar='D', nargs='+',help='directory(s) with images')

args = parser.parse_args()



if not isdir(args.out[0]):
    print("Output-directory not existant")

files = []
#Dateien in Ordnern finden
for d in args.dirs:
    files = files + [join(d,f) for f in listdir(d) if isfile(join(d, f)) if f.endswith(".png")]





BLUE = [255,0,0]        # rectangle color
YELLOW = [0,255,255]    # drawn rectangles
ORANGE = [0,128,255]


PREFERRED_WINDOW_SIZE = (800,600)
MINIMUM_WINDOW_SIZE = (200,300)

# setting up flags
rotation_angle = 0
regions = []
rect = (0,0,1,1)
rectangle = False       # flag for drawing rect
rect_over = False       # flag to check if rect drawn
input_over = False        # flag input finished
input_scale = 0.2



def drawRegions(image):
    for r in regions:
        #print(r)
        cv2.rectangle(image,(r[0:2]),(r[0]+r[2],r[1]+r[3]),YELLOW,1)

def popRegion():
    global working,img
    if len(regions) > 0:
        regions.pop()
        working = resized.copy()
        drawRegions(working)
        img = working.copy()
        
def onmouse(event,x,y,flags,param):
    global img,working,drawing,value,mask,rectangle,rect,rect_or_mask,ix,iy,rect_over
    
    xx = max(0,min(x,img.shape[1]))
    yy = max(0,min(y,img.shape[0]))
    
    # Draw Rectangle
    if event == cv2.EVENT_LBUTTONDOWN:
        rectangle = True
        rect = (0,0,1,1)
        rect_over = False
        ix,iy = xx,yy
    elif event == cv2.EVENT_RBUTTONDOWN and not rectangle: 
        popRegion()
        drawRegions(working)
        img=working.copy()
        rectangle = True
        rect = (0,0,1,1)
        rect_over = False
        ix,iy = xx,yy
    elif event == cv2.EVENT_MOUSEMOVE and rectangle:
        img = working.copy()
        cv2.rectangle(img,(ix,iy),(xx,yy),BLUE,2)
        rect = (min(ix,xx,img.shape[1]-1),min(iy,yy,img.shape[0]-1),abs(ix-xx),abs(iy-yy))

    elif event == cv2.EVENT_LBUTTONUP or cv2.EVENT_RBUTTONUP and rectangle:
        rectangle = False
        
        
        rect = (max(0,min(ix,xx,img.shape[1]-1)),max(0,min(iy,yy,img.shape[0]-1)),max(abs(ix-xx),1),max(abs(iy-yy),1))
        regions.append(rect)
        drawRegions(working)
        img = working.copy()
        cv2.rectangle(img,(ix,iy),(xx,yy),ORANGE,2)
        
        rect_over = True
        
        #print(" Now press the key 'n' a few times until no further change \n")


    # draw touchup curves
'''
    if event == cv2.EVENT_RBUTTONDOWN:
        if rect_over == False:
            print("first draw rectangle \n")
        else:
            drawing = True
            cv2.circle(img,(x,y),thickness,value['color'],-1)
            cv2.circle(mask,(x,y),thickness,value['val'],-1)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img,(x,y),thickness,value['color'],-1)
            cv2.circle(mask,(x,y),thickness,value['val'],-1)

    elif event == cv2.EVENT_RBUTTONUP:
        if drawing == True:
            drawing = False
            cv2.circle(img,(x,y),thickness,value['color'],-1)
            cv2.circle(mask,(x,y),thickness,value['val'],-1)
'''    
            
def input_over_callback():
    global input_over
    if rect_over and len(regions) > 0:
        input_over = True

def applyRotation(img):
    rmat = cv2.getRotationMatrix2D((0,0), rotation_angle,1)
    
    if rotation_angle == 90 or rotation_angle == 270:
        dsize = (img.shape[0],img.shape[1])
    else:
        dsize = (img.shape[1],img.shape[0])

    return cv2.warpAffine(img,rmat,dsize)
    
    












output = np.zeros((1,1,3)) #Resulting Image

cv2.namedWindow('output')
cv2.namedWindow('input')
cv2.setMouseCallback('input',onmouse)

for f in files:
    input_over = False
    regions.clear()
    

    image = cv2.imread(f)
    if image == None:
        break
    input_scale = max(min(PREFERRED_WINDOW_SIZE[0]/image.shape[0],PREFERRED_WINDOW_SIZE[1]/image.shape[1]),
                max(MINIMUM_WINDOW_SIZE[0]/image.shape[0],MINIMUM_WINDOW_SIZE[1]/image.shape[1]))
    print(input_scale,image.shape)
    resized = cv2.resize(image,(0,0), fx = input_scale, fy = input_scale) #Backup Image
    working = resized.copy()
    img = working.copy()
    cv2.imshow('input',img)


    #input loop on images
    while not input_over:
        #img = cv2.resize(img,(0,0), fx = input_scale, fy = input_scale)
        #rect = {x,y,w,h}
        if rect_over and not (rect[2] == 0 or rect[3] == 0):
            output = working[rect[1]:(rect[1]+rect[3]+1),rect[0]:(rect[0]+rect[2]+1),:]

            #print(rect, output.shape)
            cv2.imshow('output',output)



        k = 0xFF & cv2.waitKey(50)

        # key bindings
        if k == 27:         # esc to exit
            break
        elif k == ord('z'): # revert
            popRegion()
            img = working.copy()
        elif k == ord('c'): # clear
            working = resized.copy()
            img = working.copy()
        elif k == 13:
            input_over_callback()
        '''elif k == ord('e'): # rotate right
            rotation_angle += 90
            rotation_angle %= 360
            working = applyRotation(resized)
            img = working.copy()
            rect_over = False
        elif k == ord('q'): # rotate left
            rotation_angle -= 90
            rotation_angle %= 360
            working = applyRotation(resized)
            img = working.copy()
            rect_over = False'''

        cv2.imshow('input',img)
        #cv2.imshow('working',working)
    
    print("Hello", regions)
    for i,r in enumerate(regions):
        x1 = int(r[0] / input_scale)
        y1 = int(r[1] / input_scale)
        x2 = int((r[0] + r[2]) / input_scale)
        y2 = int((r[1] + r[3]) / input_scale)
        output = image[y1:y2+1,x1:x2+1,:]
        print("{}/{}_{}.png".format(normpath(args.out[0]),basename(f),i))
        cv2.imwrite("{}/{}_{}.png".format(normpath(args.out[0]),basename(f),i),output)




'''

#Bilder einlesen [(Dateiname,Bild)]
images = [(f,cv2.imread(f)) for f in files]
#Nur geladene Bilder behalten
images = [i for i in images if not i[1] == None]
'''

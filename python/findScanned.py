from os import listdir, open, write, close
from os.path import isfile, join

import io
import cv2
import numpy as np
import argparse
from tkinter import *


parser = argparse.ArgumentParser(description='crops and rotates scanned pages')
parser.add_argument('dirs', metavar='D', nargs='+',help='directory(s) with images')

args = parser.parse_args()


files = []

#Dateien in Ordnern finden
for d in args.dirs:
    files = files + [join(d,f) for f in listdir(d) if isfile(join(d, f)) if f.endswith(".png")]

files_iter = iter(files)


thresh=np.zeros((1,1,1),dtype=np.uint8)
eroded=np.zeros((1,1,1),dtype=np.uint8)

def colorCorrection(mat):
    #-----Converting image to LAB Color model----------------------------------- 
    lab= cv2.cvtColor(mat, cv2.COLOR_BGR2LAB)
    #cv2.imshow("lab",lab)
    
    #-----Splitting the LAB image to different channels-------------------------
    l, a, b = cv2.split(lab)
    
    #-----Applying CLAHE to L-channel-------------------------------------------
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    cl = clahe.apply(l)
    
    #-----Merge the CLAHE enhanced L-channel with the a and b channel-----------
    limg = cv2.merge((cl,a,b))
    #cv2.imshow('limg', limg)
    
    #-----Converting image from LAB Color model to RGB model--------------------
    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    return final

def show():
    global thresh
    global eroded
    thresh = cv2.inRange(blurred, (hL.get(),sL.get(),vL.get()), (hU.get(),sU.get(),vU.get()))
    
    eroded = cv2.erode(thresh,np.ones((20,20)),borderType=cv2.BORDER_REFLECT_101)
    eroded = cv2.dilate(eroded,np.ones((20,20)),borderType=cv2.BORDER_REFLECT_101)
    
    eroded = cv2.dilate(eroded,np.ones((20,20)),borderType=cv2.BORDER_REFLECT_101)
    eroded = cv2.erode(eroded,np.ones((20,20)),borderType=cv2.BORDER_REFLECT_101)
    cv2.imshow("Thresh",thresh)
    cv2.imshow("Eroded",eroded)
    #cv2.waitKey(0)




def contours():
    _,cnts, hierachy = cv2.findContours(eroded.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    # loop over the contours
    draw = resized.copy()
    for c in cnts:
        # draw the contour and show it
        br = cv2.boundingRect(c)
        print(c)
        print(br)
        #TODO seltsame Position
        
        cv2.rectangle(draw,br[0:2],br[2:4],(255,0,0))
        cv2.drawContours(draw, [c], -1, (0, 255, 0), 2)
        cv2.imshow("Image", draw)
        cv2.waitKey(100)



def nextImage():
    global files_iter, image, resized, hsl, blurred, cced
    
    try:
        next_file = next(files_iter)
    except StopIteration:
        print("No more images!")
        return
        
    image = cv2.imread(next_file)
    
    resized = cv2.resize(image,dsize=(0,0),fx=0.2,fy=0.2,interpolation=cv2.INTER_LANCZOS4 )
    #cced = colorCorrection(resized)
    #cv2.imshow("Image",cced)
    #cv2.waitKey(100)
    
    hsl = cv2.cvtColor(resized,cv2.COLOR_BGR2HSV)
    cv2.imshow("Image",hsl)
    cv2.waitKey(100)

    # find all the 'black' shapes in the image
    '''
    # convert the resized image to grayscale, blur it slightly,
    # and threshold it
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Image",gray)
    cv2.waitKey(0)
    
    '''
    blurred = cv2.GaussianBlur(hsl, (5, 5), 0)
    cv2.imshow("Image",blurred)
    cv2.waitKey(100)





#GUI

master = Tk()
#Hue from 0 to 179 http://docs.opencv.org/trunk/df/d9d/tutorial_py_colorspaces.html
hL = Scale(master,from_=0,to=179)
hL.set(21)
hL.pack(side=LEFT)
hU = Scale(master,from_=0,to=179)
hU.set(132)
hU.pack(side=LEFT)

sL = Scale(master,from_=0,to=255)
sL.set(8)
sL.pack(side=LEFT)
sU = Scale(master,from_=0,to=255)
sU.set(255)
sU.pack(side=LEFT)

vL = Scale(master,from_=0,to=255)
vL.set(19)
vL.pack(side=LEFT)
vU = Scale(master,from_=0,to=255)
vU.set(255)
vU.pack(side=LEFT)


Button(master,text="Update",command=show).pack(side=TOP)
Button(master,text="Contours",command=contours).pack(side=TOP)
Button(master,text="Next",command=nextImage).pack(side=TOP)

nextImage()
mainloop()

cv2.destroyAllWindows()
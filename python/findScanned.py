

import cv2
import numpy as np
from tkinter import *




image = cv2.imread("D:\Dokumente\Scanned Documents\Bild.png")
resized = cv2.resize(image,dsize=(0,0),fx=0.3,fy=0.3,interpolation=cv2.INTER_LANCZOS4 )
cv2.imshow("Image",resized)
cv2.waitKey(0)


# find all the 'black' shapes in the image

# convert the resized image to grayscale, blur it slightly,
# and threshold it
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
cv2.imshow("Image",gray)
cv2.waitKey(0)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow("Image",blurred)
cv2.waitKey(0)
thresh=None

def show():
    thresh = cv2.threshold(blurred, tL.get(), tU.get(), cv2.THRESH_BINARY)[1]
    cv2.imshow("Image",thresh)
    #cv2.waitKey(0)



def contours():
    (cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                                            cv2.CHAIN_APPROX_SIMPLE)
    # loop over the contours
    for c in cnts:
        # draw the contour and show it
        cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
        cv2.imshow("Image", image)
        cv2.waitKey(0)


master = Tk()
tU = Scale(master,from_=0,to=255)
tU.set(255)
tU.pack()
tL = Scale(master,from_=0,to=255)
tL.set(125)
tL.pack()
Button(master,text="Update",command=show).pack()
Button(master,text="Contours",command=contours).pack()

mainloop()
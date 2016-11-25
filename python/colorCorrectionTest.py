import cv2

#-----Reading the image-----------------------------------------------------
img = cv2.imread('Testbilder/Bild.png', 1)
resized = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
cv2.imshow("img",resized) 

#-----Converting image to LAB Color model----------------------------------- 
lab= cv2.cvtColor(resized, cv2.COLOR_BGR2LAB)
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
bgr = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
cv2.imshow('bgr', bgr)

final = cv2.GaussianBlur(bgr,(3,3),0.2)

cv2.imshow('final', final)

cv2.waitKey(0)

cv2.destroyAllWindows()

#_____END_____#
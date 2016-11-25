import cv2

def conv(c):
	converted = cv2.cvtColor(resized,c)
	#cv2.destroyAllWindows()
	for i in range(converted.shape[2]):
		cv2.namedWindow(str(i), cv2.WINDOW_NORMAL) 
		cv2.imshow(str(i),converted[:,:,i])
	cv2.imshow("Image",converted)
	print(cv2.waitKey(100))
	print("done")

image = cv2.imread("D:\Dokumente\Jugendarbeit\Konfifreizeit 2015\Bilder\DSCI0495.JPG")
resized = cv2.resize(image,dsize=(0,0),fx=0.2,fy=0.2,interpolation=cv2.INTER_CUBIC )
print("started")
cv2.imshow("Image",resized)
cv2.waitKey(100)
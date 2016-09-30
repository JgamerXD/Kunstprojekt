from os import listdir, open, write, close
from os.path import isfile, join
#from collections import dict

import argparse
import json
import io

import cv2
import numpy as np

parser = argparse.ArgumentParser(description='Analyzes images for sorting')
parser.add_argument('dirs', metavar='D', nargs='+',help='directory(s) with images')

args = parser.parse_args()




files = []

#Dateien in Ordnern finden
for d in args.dirs:
	files = files + [join(d,f) for f in listdir(d) if isfile(join(d, f))]

#Bilder einlesen [(Dateiname,Bild)]
images = [(f,cv2.imread(f)) for f in files]
#Nur geladene Bilder behalten
images = [i for i in images if not i[1] == None]


#Breite und Hoehe aller Bilder 
sizes = np.array([i[1].shape for i in images],dtype=np.float32)
#Seitenverhaeltnisse der Bilder
aspects = sizes[:,0]/sizes[:,1]

minw = np.min(sizes[:,0])
minh = np.min(sizes[:,1])

"""
- 
"""

print(sizes[:,0].mean(),sizes[:,1].mean())

print(minw, minh)

t = io.open("./test.json",mode='wt')
json.dump(dict(file="test",w=200,h=300,col=[255,0,0]),t)
t.close()

u = io.open("./test.json",mode='rt')
test = json.load(u)
u.close()

print(test.get("file"))

#print([f[0] for f in images])
#print(images)
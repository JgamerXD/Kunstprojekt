from os import listdir
from os.path import isfile, join

from collections import namedtuple
from math import *
import numpy as np
import io
import argparse
import json
from json import JSONEncoder

"""
parser = argparse.ArgumentParser(description='Analyzes images for sorting')
parser.add_argument('dirs', metavar='D', nargs='+',help='directory(s) with images')

args = parser.parse_args()
"""



"""
class ImgDat{
 public color col;
 public int w, h;
 public int origX=-1;
 public int origY=-1;
 public ArrayList<Score> scores;
 
 
 public ImgDat(color col, int w, int h)
 {
   this.col = col;
   this.w = w;
   this.h = h;
   this.scores = new ArrayList<Score>();
 }
}
"""

#class ImgDat
	

parser = argparse.ArgumentParser(description='sort using json files')
parser.add_argument('output', metavar='O', nargs=1,help='Output json file')
parser.add_argument('target', metavar='T', nargs='?',help='Target image')
parser.add_argument('dirs', metavar='D', nargs='+',help='directory(s) with json files')


args = parser.parse_args()


Score = namedtuple('Score',['x','y','score'])

class ImgDat:
    px = 0
    py = 0
    scores = []
    
    def __init__(self,id,w,h,col):
        self.id = id
        self.w = w
        self.h = h
        self.col = col

        
class ImgDatJSONEncoder(JSONEncoder)
    def default(self,obj):
        if isinstance(obj,ImgDat)
            return dict(id=obj.id,x=obj.px,y=obj.py)
        
        return json.JSONEncoder.default(self,obj)
    
images = []

files = []





#Dateien in Ordnern finden
for d in args.dirs:
	files = files + [join(d,f) for f in listdir(d) if isfile(join(d, f)) and f.endswith('.json')]

for f in files:
	jf = io.open(f)
	imgs = json.load(jf)
	jf.close()
    for i in imgs: 
        imgdat = ImgDat(f,i.get('w'),i.get('h'),i.get('col'))
        imgdat.w  = i.get('w')
        imgdat.h  = i.get('h')
        imgdat.col  = i.get('col')
        images.append(imgdat)
	
print(images)

numImages = len(images)




#TODO set from args or calculate
width = 0
height = 0


#Optimale Farben bestimmen
colorLookup = np.array((width,height,3),dtype=np.float32)

def defaultLookup():
    for i in range(width):
        temp = []
        for j in range(height):
            #h[0,179] s[0,255] v[0,255]
            temp.append(((x/width+y/height)/2*180,255,255))
            
        colorLookup.append(temp)
    

def lookupFromImage(img):
    defaultLookup()
	


#TODO Winkeleinheiten prüfen
def calcScore(image,x,y):
    #Farbe des Ziels (h)
    h = {0,0}
    #region in lookup table
    lr = colorLookup[x:x+image.w,y:y+image.h,:]
    for c in lr[:,:,0]
        h[0] += cos(c)
        h[1] += sin(c)
    #(h,s,v)
    col =  (atan2(h[0],h[1]),mean(lr[:,:,1]),mean(lr[:,:,2]))       
    
    diff = np.absolute(image.col - col)
    
    sc = diff[0] ** 4 + diff[1] ** 2 + diff[2] 
    
    return Score(x,y,sc)
        
            
def sortImages(images,w,h):
    table = np.zeroes((w,h),dtype=np.int)
    for img in images:
        current = img
        placed = False
        for sc in current.scores:
            valid = np.maximum(table[sc.x:sc.x+image.w,sc.y:sc.y+image.h]) <= 0
            if valid:
                table[sc.x:sc.x+image.w,sc.y:sc.y+image.h] = images.index(current)
                current.px = sc.x
                current.py = sc.y
     return table       
            
            
def output(images)
    outfile=args.output
    if not outfile.endswith('.json')
        outfile += '.json'
    t = io.open(outfile, mode='wt')
    json.dumps(images,cls=ImgDatJSONEncoder)
    t.close()

'''
  for(ImgDat d:images)
  {
    println("placing...");
    //Ersten Score an freier stelle wählen
    for(Score s:d.scores)
    {
       
       boolean valid = true;
       
       //Ist Stelle Frei?
       for(int i = s.x; i<s.x+d.w;i++)
         for(int j = s.y; j<s.y+d.h;j++)
         {
           valid = valid && result[i][j] == null;
         }
       //Platzieren
       //println(s.x,s.y,result[s.x][s.y],valid);
       if(valid){
         d.origX=s.x;
         d.origY=s.y;
         for(int i = s.x; i<s.x+d.w;i++)
           for(int j = s.y; j<s.y+d.h;j++)
           {
            result[i][j]=d; 
           }
         println("succesful!");
         break;
       }
    }
  }
  '''     
     
#Lookup generieren
if not args.target == None:
    lookupFromImage(args.target)
else:
    defaultLookup()

#scores berechnen
for i in images:
    scores = {}
    for x in range(0,width-image.w):
        for y in range(0,height-image.h):
            scores.append(calcScore(image,x,y))
     image.scores = sorted(scores,key=lambda s: s.score)       
            
#TODO: Größe bestimmen

sortImages(images,100,100)
output(images)


"""
class Score implements Comparable<Score>{
  public static final int INVALID = -1;
  public float value;
  public int x,y;
  
  
  public Score(int x,int y,float value)
  {
   this.x = x;
   this.y = y;
   this.value = value;
  }
      
  public int compareTo(Score other) {
    return (this.value < other.value ? -1 :
           (this.value == other.value ? 0 : 1));
  }
}
"""

"""
static final int NUM_IMAGES = 121;

static final int MIN_IMG_WIDTH = 1;
static final int MIN_IMG_HEIGHT = 1;

static final int MAX_IMG_WIDTH = 3;
static final int MAX_IMG_HEIGHT = 3;

static final float SCALE = 10;

ArrayList<ImgDat> images;
"""

"""
//Sind die Bilder sortiert?
boolean sorted = false;
Random rnd;
ImgDat current;
int area=0;
int width,height;
ImgDat[][] result;
color[][] colorLookup;
"""

"""
void setup(){
  noLoop();
  size(800,600);
  colorMode(HSB, 360,100,100);
  rnd = new Random();
  
  images = new ArrayList<ImgDat>(NUM_IMAGES);
  init();
  
  redraw();
  
}
"""

"""
void init()
{
  
  images.clear();
  area = 0;
  
  //Bilder generieren
  int iWidth,iHeight;
  
  int dwidth = (int)sqrt(NUM_IMAGES);
  
  for(int i = 0;i<NUM_IMAGES;i++)
  {
    iWidth = rnd.nextInt(MAX_IMG_WIDTH+1-MIN_IMG_WIDTH)+MIN_IMG_WIDTH;
    iHeight = rnd.nextInt(MAX_IMG_HEIGHT+1-MIN_IMG_HEIGHT)+MIN_IMG_HEIGHT;
    float c = i*360.0f/NUM_IMAGES;
    current = new ImgDat(color(rnd.nextInt(360),100,100),iWidth,iHeight); 
    //current = new ImgDat(color((int)(c),100,100),iWidth,iHeight); 
    current.origX = i % dwidth * MAX_IMG_WIDTH;
    current.origY = (int)(i / dwidth) * MAX_IMG_HEIGHT;
    images.add(current);
    area += iWidth*iHeight;
  }
  
  //Größe des Rasters bestimmen
  int size = (int)(sqrt(area)+sqrt(max(MAX_IMG_WIDTH,MAX_IMG_HEIGHT)));
  width=height=size;
  result = new ImgDat[size][size];
  
  //Farbwerte an möglichen Positionen berechnen
  colorLookup = new color[size][size];
  for(int x = 0;x<width;x++)
    for(int y = 0;y<height;y++)
      colorLookup[x][y] = getOptimalColor(width,height,x,y);
  
  
  
}
"""

"""
void sort()
{
  println("sorting...");
  boolean placed = false;
  int bestX = 0,bestY = 0;
  
  
  //Wertung durch vergleichen der Farbtöne ermitteln
  for(ImgDat d:images)
  {
   float dhue = hue(d.col);
   for(int x = 0;x<=width-d.w;x++)
    for(int y = 0;y<=height-d.h;y++)
    {
      float rhuex=0,rhuey=0;
      
      //Durchschnittliche Farbe unter dem Rechteck bei (x|y) berechnen
       for(int i = 0; i<d.w;i++)
         for(int j = 0; j<d.h;j++)
         {
           float h = hue(colorLookup[x+i][y+j])/180*PI;
           rhuex += cos(h);
           rhuey += sin(h);
         }
      //println((atan2(rhuey,rhuex)/PI*180+360)%360);
      d.scores.add(new Score(x,y,pow(abs(dhue-(atan2(rhuey,rhuex)/PI*180+360)%360.0),3)));
    }
    //Sortieren: Gut->Schlecht
    Collections.sort(d.scores);
  }
  
  for(ImgDat d:images)
  {
    println("placing...");
    //Ersten Score an freier stelle wählen
    for(Score s:d.scores)
    {
       
       boolean valid = true;
       
       //Ist Stelle Frei?
       for(int i = s.x; i<s.x+d.w;i++)
         for(int j = s.y; j<s.y+d.h;j++)
         {
           valid = valid && result[i][j] == null;
         }
       //Platzieren
       //println(s.x,s.y,result[s.x][s.y],valid);
       if(valid){
         d.origX=s.x;
         d.origY=s.y;
         for(int i = s.x; i<s.x+d.w;i++)
           for(int j = s.y; j<s.y+d.h;j++)
           {
            result[i][j]=d; 
           }
         println("succesful!");
         break;
       }
    }
  }
  
  println("finished!");
}
"""

"""
//Store in lookup-table for sorting
color getOptimalColor(float w,float h,float x,float y)
{
 return color((int)((x/w+y/h)/2*360),100,100);
}
"""
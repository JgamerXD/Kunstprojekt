/**
 * Test program written in Processing 3
 **/

import java.util.*;

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


static final int NUM_IMAGES = 121;

static final int MIN_IMG_WIDTH = 1;
static final int MIN_IMG_HEIGHT = 1;

static final int MAX_IMG_WIDTH = 3;
static final int MAX_IMG_HEIGHT = 3;

static final float SCALE = 10;

ArrayList<ImgDat> images;

//Sind die Bilder sortiert?
boolean sorted = false;
Random rnd;
ImgDat current;
int area=0;
int width,height;
ImgDat[][] result;
color[][] colorLookup;

void setup(){
  noLoop();
  size(800,600);
  colorMode(HSB, 360,100,100);
  rnd = new Random();
  
  images = new ArrayList<ImgDat>(NUM_IMAGES);
  init();
  
  redraw();
  
}

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

void mouseClicked()
{
  if(sorted)
    init();
  else
    sort(); 
  sorted = !sorted;
  redraw();
}

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

//Store in lookup-table for sorting
color getOptimalColor(float w,float h,float x,float y)
{
 return color((int)((x/w+y/h)/2*360),100,100);
}

void draw(){
  background(50);
  pushMatrix();
  
  translate(20,20);
  
  scale(SCALE);
  
  
  if(sorted){
    //Raster
    strokeWeight(0.1);
    stroke(255);
    fill(50);
    for(int i = 0;i<width;i++)
      for(int j = 0;j<height;j++)
        rect(i,j,1,1);
      
  }
  noStroke();
  //Bilder
  for(ImgDat d:images)
    {
      if(d.origX > -1 && d.origY > -1)
      {
        //println(d.col);
        fill(d.col);
        //stroke(d.col);
        rect(d.origX,d.origY,d.w,d.h);
      }
    }
    
  //Referenz
  translate((int)sqrt(NUM_IMAGES)*MAX_IMG_WIDTH+10,0);
  scale(0.1);
  strokeWeight(1);
  for(int i = 0;i<width*10;i++)
    for(int j = 0;j<height*10;j++)
      {
        //fill(getOptimalColor(width,height,i/10.0f,j/10.0f));
        stroke(getOptimalColor(width,height,i/10.0f,j/10.0f));
        point(i,j);
      }
      
  popMatrix();
}
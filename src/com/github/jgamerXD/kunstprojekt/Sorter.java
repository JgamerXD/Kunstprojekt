package com.github.jgamerXD.kunstprojekt;

import java.awt.*;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by Janki on 14.09.2016.
 */
class SortingData
{
    public static final int INVALID_POSITION = -1;

    //Informationen über das Bild
    ImageData image;

    //Position des Bildes
    int posX, posY;

    //Bewertungen einzelner positionen
    List<Score> scores;

    public SortingData(ImageData image) {
        this.image = image;
        scores = new ArrayList<Score>();
    }

    public SortingData(ImageData image, int posX, int posY, List<Score> scores) {
        this.image = image;
        this.posX = posX;
        this.posY = posY;
        this.scores = scores;
    }
}

class Score implements Comparable<Score>{
    float score;
    int posX,posY;

    public Score(float score, int posX, int posY) {
        this.score = score;
        this.posX = posX;
        this.posY = posY;
    }

    @Override
    public int compareTo(Score o) {
        return Float.compare(this.score,o.score);
    }
}

public class Sorter {
    SortingData[][] result;
    List<SortingData> toBePlaced;
    Color[][] optimalColors;

    public Sorter(ImageData[] images,Image target){

        toBePlaced = new ArrayList<SortingData>(images.length);

        int minW = Integer.MAX_VALUE,
                maxW = Integer.MIN_VALUE,
                minH = Integer.MAX_VALUE,
                maxH = Integer.MIN_VALUE;
        int area = 0;

        for(ImageData id : images){
            toBePlaced.add(new SortingData(id));
            minW = Math.min(minW,id.w);
            maxW = Math.max(maxW,id.w);
            minW = Math.min(minW,id.h);
            maxH = Math.max(maxH,id.h);
            area += id.w*id.h;
        }

        int sizeX = (int)(Math.sqrt(area)*target.getWidth(null)/target.getHeight(null)+minW);
        int sizeY = area/sizeX + minH;

        result = new SortingData[sizeX][sizeY];
        optimalColors = new Color[sizeX][sizeY];

        //TOD
    }

}

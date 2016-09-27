package jgamerXD.kunstprojekt;

import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.core.Scalar;

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
    Scalar[][] optimalColors;

    public Sorter(ImageData[] images,Mat target){

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
            minH = Math.min(minW,id.h);
            maxH = Math.max(maxH,id.h);
            area += id.w*id.h;
        }


        int sizeX = ((int)(Math.sqrt(area)*(target.cols()/4)/target.rows()+minW));
        int sizeY = (area/sizeX + minH);

        result = new SortingData[sizeX][sizeY];
        optimalColors = new Scalar[sizeX][sizeY];


//
//        int startcol = 0;
//        int endcol = (target.cols()/4)/((i+1)/sizeX)*4;
//        int startrow = 0;
//        int endrow = target.rows()/((i+1)/sizeX);

        for (int i = 0; i < optimalColors.length; i++) {
            int startrow = target.rows()*(i/sizeX);
            int endrow = target.rows()*((i+1)/sizeX);

            for (int j = 0; j < optimalColors[i].length; j++) {
                int startcol = target.cols()*(i/sizeX);
                int endcol = (target.cols()/4)*((i+1)/sizeX)*4;

                optimalColors[i][j] = Core.mean(target.submat(startrow,endrow,startcol,endcol));
            }

        }


        System.out.println(optimalColors);
    }

}

package jgamerXD.kunstprojekt;

import jdk.nashorn.internal.ir.debug.JSONWriter;
import jdk.nashorn.internal.objects.Global;
import jdk.nashorn.internal.parser.JSONParser;
import jdk.nashorn.internal.runtime.JSONFunctions;
import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.core.Scalar;

import java.awt.*;
import java.io.IOException;
import java.net.URL;
import java.util.UUID;

/**
 * Created by Janki on 14.09.2016.
 */
public class ImageData {

    public final long id; //TODO: Notwendig/Sinnvoll?
    public int w,h; //Breite / Höhe des Bildes
    public Scalar col; //Durchschnittsfarbe TODO: einzeln für jedes Rasterfeld?
    Mat image;


    public ImageData(long id, int w, int h, Scalar col) {
        this.id=id;
        this.w = w;
        this.h = h;
        this.col = col;
    }

    public ImageData(long id) {
        this.id=id;
        this.col = new Scalar(0,0,0,0);
        this.w=0;
        this.h=0;
    }
}

package com.github.jgamerXD.kunstprojekt;

import jdk.nashorn.internal.ir.debug.JSONWriter;
import jdk.nashorn.internal.objects.Global;
import jdk.nashorn.internal.parser.JSONParser;
import jdk.nashorn.internal.runtime.JSONFunctions;
import org.opencv.core.Core;
import org.opencv.core.Mat;

import java.awt.*;
import java.io.IOException;
import java.net.URL;
import java.util.UUID;

/**
 * Created by Janki on 14.09.2016.
 */
public class ImageData {

    public final UUID image; //Referenz zum Bild TODO: recource manager?
    public final String file; //TODO: Notwendig/Sinnvoll?
    public int w,h; //Breite / Höhe des Bildes im Raster
    public Color col; //Durchschnittsfarbe TODO: einzeln für jedes Rasterfeld?



    public ImageData(UUID image, String file, int w, int h, Color col) {
        this.image = image;
        this.file = file;
        this.w = w;
        this.h = h;
        this.col = col;
    }

    public ImageData(Mat mat, String file) {
        image = new UUID(0,0);
        this.file = file;

        w = mat.cols()/4;
        h = mat.rows();
        double[] color = Core.mean(mat).val;
        //In Java Color umwandeln (von ABGR)
        System.out.println(mat.channels());
        col = new Color((float)color[2],(float)color[1],(float)color[0]);
    }
}

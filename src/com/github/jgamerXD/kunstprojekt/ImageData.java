package com.github.jgamerXD.kunstprojekt;

import java.awt.*;
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
}

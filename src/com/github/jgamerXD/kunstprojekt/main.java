package com.github.jgamerXD.kunstprojekt;

/**
 * Created by Janki on 09.09.2016.
 */

import com.sun.org.apache.xerces.internal.xs.StringList;
import org.opencv.core.*;
import org.opencv.imgcodecs.Imgcodecs;

import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;


class main {

    static {
        System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
    }

    public static void main(String[] args) {

        /*EventQueue.invokeLater(() -> {
            JFrame frame = new Viewport();
            frame.setSize(600, 800);

            //Display the window.
            frame.pack();
            frame.setVisible(true);
        });*/

        String[] exts = new String[] {".jpg"};


        LoadImages.load("images", Arrays.asList(exts));


    }

}

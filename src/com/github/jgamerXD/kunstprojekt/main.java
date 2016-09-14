package com.github.jgamerXD.kunstprojekt;

/**
 * Created by Janki on 09.09.2016.
 */

import com.github.jgamerXD.kunstprojekt.gui.Viewport;
import org.opencv.core.*;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.objdetect.CascadeClassifier;

import javax.swing.*;
import java.awt.*;
import java.util.Scanner;



class main {

    static {
        System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
    }

    public static void main(String[] args) {

        EventQueue.invokeLater(() -> {
            JFrame frame = new Viewport();
            frame.setSize(600, 800);

            //Display the window.
            frame.pack();
            frame.setVisible(true);
        });

        Mat mat = Imgcodecs.imread("spider-oben.jpg");

        System.out.println(mat);


    }

}

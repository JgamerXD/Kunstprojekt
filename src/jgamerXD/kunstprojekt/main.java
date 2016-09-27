package jgamerXD.kunstprojekt;

/**
 * Created by Janki on 09.09.2016.
 */

import jgamerXD.kunstprojekt.gui.Viewport;
import org.opencv.core.*;

import javax.swing.*;
import java.awt.*;
import java.util.Arrays;


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

        String[] exts = new String[] {".jpg"};


        ImageLoader.load("images", Arrays.asList(exts));


    }

}

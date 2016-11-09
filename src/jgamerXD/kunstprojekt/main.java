package jgamerXD.kunstprojekt;

/**
 * Created by Janki on 09.09.2016.
 */

import jgamerXD.kunstprojekt.gui.ResourceManager;
import jgamerXD.kunstprojekt.gui.Viewport;
import org.opencv.core.*;

import javax.swing.*;
import java.awt.*;
import java.util.Arrays;
import java.util.concurrent.locks.ReentrantReadWriteLock;


class main {

    static Viewport viewport;
    static DataManager dataManager = new DataManager();

    static {
        System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
    }

    public static void main(String[] args) {


        EventQueue.invokeLater(() -> {
            JFrame frame = new Viewport(dataManager);
            frame.setSize(640, 800);

            //Display the window.
            frame.pack();
            frame.setVisible(true);
        });

        String[] exts = new String[] {".jpg"};
        dataManager.images.addAll(dataManager.resources.loadfromDirectory("images", Arrays.asList(exts)));



    }

}

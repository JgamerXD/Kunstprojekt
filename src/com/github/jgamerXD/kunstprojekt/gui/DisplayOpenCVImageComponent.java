package com.github.jgamerXD.kunstprojekt.gui;

import org.opencv.core.Mat;
import org.opencv.core.MatOfByte;
import org.opencv.imgcodecs.Imgcodecs;

import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.InputStream;

/**
 * Created by Janki on 09.09.2016.
 */
public class DisplayOpenCVImageComponent extends JLabel {
    public DisplayOpenCVImageComponent(String image) {
        super();
//        Mat image_tmp = Imgcodecs.imread(image);
//        System.out.println(image_tmp.get(0,0));
//
//        MatOfByte matOfByte = new MatOfByte();
//
//        Imgcodecs.imencode(".jpg", image_tmp, matOfByte);
//
//        byte[] byteArray = matOfByte.toArray();
//        BufferedImage bufImage = null;
//
//        try {
//
//            InputStream in = new ByteArrayInputStream(byteArray);
//            bufImage = ImageIO.read(in);
//        } catch (Exception e) {
//            e.printStackTrace();
//        }
//        setIcon(new ImageIcon(bufImage));
    }

    public DisplayOpenCVImageComponent() {
        super();
    }
}

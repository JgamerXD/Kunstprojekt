package jgamerXD.kunstprojekt.gui;

import jgamerXD.kunstprojekt.OpenCVUtils;
import org.opencv.core.Mat;

import javax.swing.*;

/**
 * Created by Janki on 09.09.2016.
 */
public class DisplayOpenCVImageComponent extends JLabel {
    public DisplayOpenCVImageComponent(Mat image) {
        super();
        Icon icon = new ImageIcon(OpenCVUtils.Mat2BufferedImage(image));
        //setSize(icon.getIconWidth(),icon.getIconHeight());
        setIcon(icon);

    }

    public DisplayOpenCVImageComponent() {
        super();
    }
}

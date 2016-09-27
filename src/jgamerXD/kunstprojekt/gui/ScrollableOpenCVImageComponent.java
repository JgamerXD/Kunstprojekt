package jgamerXD.kunstprojekt.gui;

import jgamerXD.kunstprojekt.OpenCVUtils;
import org.opencv.core.Mat;
import org.opencv.core.Size;
import org.opencv.imgproc.Imgproc;

import javax.swing.*;
import java.awt.event.ComponentEvent;
import java.awt.event.ComponentListener;
import java.awt.event.MouseWheelEvent;
import java.awt.event.MouseWheelListener;

/**
 * Created by Janki on 27.09.2016.
 */
public class ScrollableOpenCVImageComponent extends JScrollPane implements MouseWheelListener {
    JLabel content = new JLabel();
    Mat image;
    double scale = 1;


    public ScrollableOpenCVImageComponent(Mat image) {
        super();
        this.image = image;
        this.add(content);
        this.updateIcon();
    }

    public ScrollableOpenCVImageComponent() {
        super();
        this.image=new Mat();
        this.add(content);
    }

    public void setImage(Mat image)
    {
        this.image=image;
        updateIcon();
    }

    public void updateIcon()
    {
        Mat tmp = new Mat();
        Imgproc.resize(image,tmp,new Size(),scale,scale,Imgproc.INTER_CUBIC);
        Icon icon = new ImageIcon(OpenCVUtils.Mat2BufferedImage(tmp));
        content.setIcon(icon);
    }


    @Override
    public void mouseWheelMoved(MouseWheelEvent e) {
        scale += e.getScrollAmount()*scale/10.0;
    }
}

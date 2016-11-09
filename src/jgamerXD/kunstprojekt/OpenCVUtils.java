package jgamerXD.kunstprojekt;

import org.opencv.core.Mat;
import org.opencv.core.Scalar;
import org.opencv.imgcodecs.Imgcodecs;

import java.awt.*;
import java.awt.image.BufferedImage;
import java.awt.image.DataBufferByte;
import java.io.File;
import java.util.Arrays;

/**
 * Created by Janki on 26.09.2016.
 */
public class OpenCVUtils {
    public static BufferedImage Mat2BufferedImage(Mat m){
// source: http://answers.opencv.org/question/10344/opencv-java-load-image-to-gui/
// Fastest code
// The output can be assigned either to a BufferedImage or to an Image

        int type = BufferedImage.TYPE_BYTE_GRAY;
        if ( m.channels() > 1 ) {
            type = BufferedImage.TYPE_3BYTE_BGR;
        }
        int bufferSize = m.channels()*m.cols()*m.rows();
        byte [] b = new byte[bufferSize];
        m.get(0,0,b); // get all the pixels
        BufferedImage image = new BufferedImage(m.cols(),m.rows(), type);
        final byte[] targetPixels = ((DataBufferByte) image.getRaster().getDataBuffer()).getData();
        System.arraycopy(b, 0, targetPixels, 0, b.length);
        return image;

    }

    public static Mat readFile(File f)
    {
        return Imgcodecs.imread(f.getAbsolutePath());
    }

    public static Color scalarToColor(Scalar scalar)
    {
        double[] values = scalar.val;
        for (int i = 0; i < values.length; i++) {
            values[i] /= 255.0;
        }
        return new Color((float) values[2],(float)values[1],(float)values[0]);
    }
}

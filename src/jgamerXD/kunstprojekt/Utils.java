package jgamerXD.kunstprojekt;

import javax.swing.*;
import java.awt.geom.AffineTransform;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.util.Scanner;

/**
 * Created by By_if1_08 on 09.06.2016.
 */
public class Utils {
    public static URL getResourceURL(String fileName) {
        URL url = null;

        try {
            //Get file from resources folder
            ClassLoader classLoader = Thread.currentThread().getContextClassLoader();
            url = classLoader.getResource(fileName);
        }
        catch (Exception e)
        {
            System.err.println("Error while loading resource (" + fileName + ")");
            e.printStackTrace(System.err);
        }
        return url;
    }


    public static File getResourceFile(String fileName) {
        File file = null;

        try {
            //Get file from resources folder
            ClassLoader classLoader = Thread.currentThread().getContextClassLoader();
            file = new File(classLoader.getResource(fileName).getFile());
        } catch (Exception e) {
            System.err.println("Error while loading resource (" + fileName + ")");
            e.printStackTrace(System.err);
        }
        return file;

    }

    public static int toXReal(JComponent component,double val)
    {
        return (int)(val * (component.getWidth()-1));
    }

    public static int toYReal(JComponent component,double val)
    {
        return (int)(val * (component.getHeight()-1));
    }

    public static AffineTransform getTransform(JComponent component, float centerX, float centerY, float scale, float rotation)
    {
        float sc = Math.min(component.getWidth(),component.getHeight())/scale;
        float tx = component.getWidth()/2.0f;
        float ty = component.getHeight()/2.0f;

        return  new AffineTransform(
                (sc * Math.cos(rotation)),(-sc * Math.sin(rotation)),(centerX*sc*Math.cos(rotation)-centerY*sc*Math.sin(rotation)+tx),
                (sc * Math.sin(rotation)),(sc * Math.cos(rotation)),(centerX*sc*Math.sin(rotation)+centerY*sc*Math.cos(rotation)+ty));
    }

    public static String readFile(String fileName) throws IOException
    {
        ClassLoader classloader = Thread.currentThread().getContextClassLoader();
        InputStream is = classloader.getResourceAsStream(fileName);
        if (is == null) {
            throw new IOException(fileName + " is not a valid resource");
        }
        Scanner sc = new Scanner(is).useDelimiter("\\A");
        return sc.next();

    }

    public static double clamp(double val, double min, double max) {

        if (val < min) {
            return min;
        }
        if (val > max) {
            return max;
        }
        return val;
    }

    public static int clamp(int val, int min, int max) {

        if (val < min) {
            return min;
        }
        if (val > max) {
            return max;
        }
        return val;
    }

}

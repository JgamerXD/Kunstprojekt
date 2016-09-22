package com.github.jgamerXD.kunstprojekt;

import org.opencv.core.Mat;
import org.opencv.imgcodecs.Imgcodecs;

import java.io.File;
import java.io.FilenameFilter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by Janki on 15.09.2016.
 */
public class LoadImages {
    public static final String ROOT_DIR = "\\res\\";



    static void load(String folder,List<String> extensions)
    {
        File dir = Utils.getResourceFile(folder);


        List<Mat> mats = new ArrayList<>();

        File[] files = dir.listFiles(n -> n.isFile()&& n.canRead());

        for (File file : files) {
            String name = file.toString();
            if(extensions.contains(name.substring(name.lastIndexOf("."))))
                mats.add(Imgcodecs.imread(name));
        }
        System.out.println(mats.add(Imgcodecs.imread("res\\images\\spider-oben.jpg")));
        mats.forEach(System.out::println);
        System.out.println("Hi");

        ImageData[] data = new ImageData[mats.size()];
        for (int i = 0; i < mats.size(); i++) {
            data[i] = new ImageData(mats.get(i),files[i].toString());
        }

        Sorter s = new Sorter(data,mats.get(0));
    }
}

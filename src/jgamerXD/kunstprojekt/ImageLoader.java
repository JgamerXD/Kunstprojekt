package jgamerXD.kunstprojekt;

import org.opencv.core.Mat;
import org.opencv.imgcodecs.Imgcodecs;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by Janki on 15.09.2016.
 */
public class ImageLoader {



    public static List<Mat> loadfromDirectory(String folder,List<String> extensions)
    {
        File dir = Utils.getResourceFile(folder);


        List<Mat> mats = new ArrayList<>();
        List<File> files = new ArrayList<>();

        File[] tmpFiles = dir.listFiles(n -> n.isFile()&& n.canRead());

        for (File file : tmpFiles) {
            String name = file.toString();
            if(extensions.contains(name.substring(name.lastIndexOf(".")))){
                Mat mat = Imgcodecs.imread(name);
                if(!mat.empty()) {
                    mats.add(mat);
                    files.add(file);
                }
            }

        }
//        //System.out.println(mats.add(Imgcodecs.imread("res\\images\\spider-oben.jpg")));
//        mats.forEach(System.out::println);
//        //System.out.println("Hi");
//
//        int size = mats.size();
//        ImageData[] data = new ImageData[size];
//        for (int i = 0; i < size; i++) {
//            //System.out.printf("-----%d%n",size);
//            data[i] = new ImageData(mats.get(i),files.get(i).toString());
//        }

        return mats;
    }

    public static Mat loadFromFile(String file){
        return Imgcodecs.imread(Utils.getResourceFile(file).getAbsolutePath());
    }

    public static Mat loadFromFile(File file){
        return Imgcodecs.imread(file.getAbsolutePath());
    }
}

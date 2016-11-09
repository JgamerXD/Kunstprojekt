package jgamerXD.kunstprojekt.gui;

import com.sun.istack.internal.NotNull;
import jgamerXD.kunstprojekt.ImageData;
import jgamerXD.kunstprojekt.ImageLoader;
import jgamerXD.kunstprojekt.Utils;
import org.opencv.core.Mat;
import org.opencv.imgcodecs.Imgcodecs;

import java.io.File;
import java.io.IOException;
import java.util.*;

/**
 * Created by Janki on 27.09.2016.
 */
public class ResourceManager {
    Map<Long,Mat> images = new HashMap<>();
    Map<String,Long> files = new HashMap<>();

    long lastID = 0;

    public long add(@NotNull Mat mat)
    {
        long id = ++lastID;
        images.put(id,mat);
        return id;
    }

    public long add(Mat mat, String file){
        long id;
        String f = file;//Utils.getResourceFile(file).getAbsolutePath();
        if(files.containsKey(f))
        {
            if(images.containsKey(files.get(f)))
                return files.get(f);
            else id = files.get(f);
        }
        else
            id = ++lastID;

        files.put(f,id);
        images.put(id,mat);
        return id;
    }

    public long load(String file)
    {
        long id;
        String f = Utils.getResourceFile(file).getAbsolutePath();
        if(files.containsKey(f))
        {
            if(images.containsKey(files.get(f)))
                return files.get(f);
            else id = files.get(f);
        }
        else
            id = ++lastID;

        try{
            Mat mat = Imgcodecs.imread(f);
            if(mat.empty())
            {
                throw new IOException("Image Empty");
            }
//            long id = ++lastID;
            images.put(id,mat);
            files.put(f,id);
            return id;
        }
        catch (Exception e)
        {
            System.out.printf("Could not load %s%n",f);
            e.printStackTrace();
        }
        return -1;
    }

    public Mat getImage(long id)
    {
        return images.get(id);
    }

    public void freeImage(long id)
    {
        images.remove(id);
    }

    public List<ImageData> loadfromDirectory(String folder,List<String> extensions) {
        File dir = Utils.getResourceFile(folder);


        List<ImageData> result = new ArrayList<>();

        File[] tmpFiles = dir.listFiles(n -> n.isFile() && n.canRead());

        for (File file : tmpFiles) {
            String name = file.toString();
            if (extensions.contains(name.substring(name.lastIndexOf(".")))) {
                Mat mat = Imgcodecs.imread(name);
                if (!mat.empty()) {
                    result.add(new ImageData(add(mat,file.getAbsolutePath())));
                }
            }

        }
        return result;
    }

//    public Collection<Mat> getImages()
//    {
//        return images.values();
//    }
}

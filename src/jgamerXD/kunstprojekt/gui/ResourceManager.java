package jgamerXD.kunstprojekt.gui;

import com.sun.istack.internal.NotNull;
import jgamerXD.kunstprojekt.ImageData;
import jgamerXD.kunstprojekt.ImageLoader;
import jgamerXD.kunstprojekt.Utils;
import org.opencv.core.Mat;
import org.opencv.imgcodecs.Imgcodecs;

import java.io.File;
import java.io.IOException;
import java.util.Map;

/**
 * Created by Janki on 27.09.2016.
 */
public class ResourceManager {
    Map<Long,Mat> images;
    Map<String,Long> files;

    long lastID = 0;

    public long add(@NotNull Mat mat)
    {
        long id = ++lastID;
        images.put(id,mat);
        return id;
    }

    public long load(String file)
    {
        String f = Utils.getResourceFile(file).getAbsolutePath();
        if(files.containsKey(f))
        {
            return files.get(f);
        }

        try{
            Mat mat = Imgcodecs.imread(f);
            if(mat.empty())
            {
                throw new IOException("Image Empty");
            }
            long id = ++lastID;
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


}

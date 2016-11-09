package jgamerXD.kunstprojekt;

import jgamerXD.kunstprojekt.gui.ResourceManager;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

/**
 * Created by Janki on 27.09.2016.
 */
public class DataManager{
    public ResourceManager resources = new ResourceManager();
    public List<ImageData> images = new ArrayList<>();

    public Collection<ImageData> getImages(){
        return images;
    }

}

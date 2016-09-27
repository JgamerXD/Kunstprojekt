package jgamerXD.kunstprojekt;

import java.util.ArrayList;
import java.util.List;

/**
 * Images with positions
 */
public class ImageMap {
    private class PositionedImage {
        float posX,posY;
        ImageData image;

        public PositionedImage(float posX, float posY, ImageData image) {
            this.posX = posX;
            this.posY = posY;
            this.image = image;
        }
    }

    List<PositionedImage> data;

    public ImageMap(ImageData[] images, float[] x, float[] y) {

        assert(images.length == x.length && x.length == y.length);

        data = new ArrayList<>(images.length);

        for (int i = 0; i < images.length; i++) {
            data.add(new PositionedImage(x[i],y[i],images[i]));
        }
    }
}

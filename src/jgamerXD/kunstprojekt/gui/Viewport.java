package jgamerXD.kunstprojekt.gui;

import jgamerXD.kunstprojekt.DataManager;
import jgamerXD.kunstprojekt.OpenCVUtils;
import jgamerXD.kunstprojekt.Utils;

import javax.swing.*;
import java.awt.*;
import java.util.HashMap;
import java.util.Map;

/**
 * Created by Janki on 08.09.2016.
 */
public class Viewport extends JFrame{
    private JPanel mainPanel;
    private JButton button1;
    private JPanel content;
    private DisplayOpenCVImageComponent displayOpenCVImageComponent1;

    Map<String,JPanel> views = new HashMap<>();

    public final DataManager data;

    public Viewport() throws HeadlessException {
        super("Kunstprojekt");
        data = new DataManager();

        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        setContentPane(mainPanel);
    }

    private void init()
    {
        views.put("browse", new BrowseImages(this));
    }

    private void createUIComponents() {
        displayOpenCVImageComponent1 = new DisplayOpenCVImageComponent(OpenCVUtils.readFile(Utils.getResourceFile("./images/spider-oben.jpg")));
    }
}

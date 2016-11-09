package jgamerXD.kunstprojekt.gui;

import jgamerXD.kunstprojekt.DataManager;
import jgamerXD.kunstprojekt.ImageLoader;
import jgamerXD.kunstprojekt.OpenCVUtils;
import jgamerXD.kunstprojekt.Utils;

import javax.swing.*;
import java.awt.*;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * Created by Janki on 08.09.2016.
 */
public class Viewport extends JFrame{
    private JPanel mainPanel;
    private JButton button1;
    private JPanel content;
    private JTextArea halloTestDsihfakjgflsdhgbkhsevklufhkavhvahvahavehklelvflbaTextArea;
    private DisplayOpenCVImageComponent displayOpenCVImageComponent1;

    Map<String,JPanel> views = new HashMap<>();

    public final DataManager data;

    public Viewport(DataManager manager) throws HeadlessException {
        super("Kunstprojekt");
        data = manager;

        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        setContentPane(mainPanel);

        views.put("browse", new BrowseImages(this));

        setView("browse");
    }


    public boolean setView(String name)
    {
        if(!views.containsKey(name))
            return false;
        content.removeAll();
        JComponent p = views.get(name);
        content.add(p);
        return true;
    }

    private void createUIComponents() {


        displayOpenCVImageComponent1 = new DisplayOpenCVImageComponent(OpenCVUtils.readFile(Utils.getResourceFile("./images/spider-oben.jpg")));
    }


}

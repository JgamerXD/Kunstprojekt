package com.github.jgamerXD.kunstprojekt.gui;

import javax.swing.*;
import java.awt.*;

/**
 * Created by Janki on 08.09.2016.
 */
public class Viewport extends JFrame{
    private JPanel mainPanel;
    private JButton button1;
    private DisplayOpenCVImageComponent displayOpenCVImageComponent1;

    public Viewport() throws HeadlessException {
        super("Kunstprojekt");
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        setContentPane(mainPanel);
    }

    private void createUIComponents() {
        displayOpenCVImageComponent1 = new DisplayOpenCVImageComponent("/lena.png");
    }
}

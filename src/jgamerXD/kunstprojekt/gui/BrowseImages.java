package jgamerXD.kunstprojekt.gui;

import javax.swing.*;

/**
 * Created by Janki on 27.09.2016.
 */
public class BrowseImages extends JPanel{
    private JList images;
    private JTextPane informationPanel;
    private JPanel colorPanel;
    private JLabel colorLabel;
    private JPanel mainPanel;

    private Viewport viewport;

    public BrowseImages(Viewport viewport) {
        this.viewport = viewport;
        this.add(mainPanel);
    }

    private void createUIComponents() {
        // TODO: place custom component creation code here
    }
}

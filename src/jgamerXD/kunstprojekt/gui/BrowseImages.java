package jgamerXD.kunstprojekt.gui;

import javafx.scene.control.SelectionMode;
import javafx.scene.control.SelectionModel;
import jgamerXD.kunstprojekt.ImageData;
import jgamerXD.kunstprojekt.OpenCVUtils;

import javax.swing.*;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;

/**
 * Created by Janki on 27.09.2016.
 */
public class BrowseImages extends JPanel implements ListSelectionListener{
    private JList images;
    private JTextPane informationPanel;
    private JPanel colorPanel;
    private JLabel colorLabel;
    private JPanel mainPanel;

    private Viewport viewport;

    public BrowseImages(Viewport viewport) {
        this.viewport = viewport;
        this.add(mainPanel);

        images.setListData(viewport.data.getImages().toArray());

    }

    private void createUIComponents() {
        // TODO: place custom component creation code here
        images = new JList(new DefaultListModel<ImageData>());
        images.addListSelectionListener(this);
        images.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        images.setListData(viewport.data.getImages().toArray());
    }

    @Override
    public void valueChanged(ListSelectionEvent e) {
        ImageData selected = (ImageData) images.getSelectedValue();
        colorPanel.setBackground(OpenCVUtils.scalarToColor(selected.col));
    }
}

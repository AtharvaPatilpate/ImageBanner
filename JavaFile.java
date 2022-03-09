import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.io.File;

import javax.imageio.ImageIO;

public class JavaFile {
    public static void main(String[] args) throws Exception {

        // read the image
        BufferedImage image = ImageIO.read(new File("Picture1.png"));

        // get the Graphics object
        Graphics g = image.getGraphics();

        // set font
        g.setColor(Color.BLACK);
        g.setFont(new Font("Calibri", Font.PLAIN, 100));

        // display the text at the coordinates
        write(g);

        // write the image
        ImageIO.write(image, "png", new File("image1.png"));
    }

    private static void write(Graphics g) {
        g.drawString("Atharva Patilpate", 50, 1650);
        g.drawString("Pune", 50, 1750);
        g.drawString("9999999999", 50, 1850);
        g.dispose();
    }
}

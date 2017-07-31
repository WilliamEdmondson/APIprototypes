/* @pjs preload="./static/out.csv"; */
Table table;


void setup() {

  // The window
  size(512, 512);
  noLoop();
}

void draw() {
    int side = 512;
    // pixel data
    table = loadTable("/static/out.csv");

    // Blank Image
    PImage img = createImage(side, side, ALPHA);


    loadPixels();
    for(int x = 0; x < side; x++) {
        for(int y = 0; y < side; y++) {
          int loc = x + y*side;
          int grey = int(table.getInt(x,y)/8);
          pixels[loc] = grey;
        }
    }
  updatePixels();
}

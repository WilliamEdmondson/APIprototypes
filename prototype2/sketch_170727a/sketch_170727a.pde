
PImage img;

void setup() {
  
  // The window
  int side = 512;
  size(512, 512);
  
  // pixel data
  Table table;
  table = loadTable("out.csv");
  
  // Blank Image
  PImage img = createImage(side, side, ALPHA);
  
  
  loadPixels();
  for(int x = 0; x < side; x++) {
      for(int y = 0; y < side; y++) {
        int loc = x + y*side;
        int grey = table.getInt(x,y)/8;
        pixels[loc] = grey;
      }
  }
updatePixels();
    
  
}

void draw() {
  
}


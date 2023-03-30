#include <math.h>
#include <SPI.h> 
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

#define OLED_RESET -1
#define SCREEN_ADDRESS 0x3c
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

#define TILE_SIZE 8

static const unsigned char PROGMEM bike_up_bmp[] =
 { 0b00011000,
   0b00011000,
   0b00100100,
   0b00100100,
   0b00111100,
   0b00111100,
   0b00011000,
   0b00000000};

static const unsigned char PROGMEM bike_left_bmp[] =
 { 0b00000000,
   0b00000000,
   0b00111100,
   0b11001110,
   0b11001110,
   0b00111100,
   0b00000000,
   0b00000000};

static const unsigned char PROGMEM bike_down_bmp[] =
 { 0b00000000,
   0b00011000,
   0b00111100,
   0b00111100,
   0b00100100,
   0b00100100,
   0b00011000,
   0b00011000};

static const unsigned char PROGMEM bike_right_bmp[] =
 { 0b00000000,
   0b00000000,
   0b00111100,
   0b01110011,
   0b01110011,
   0b00111100,
   0b00000000,
   0b00000000};

static const unsigned char PROGMEM path_up_bmp[] =
 { 0b00011000,
   0b00011000,
   0b00011000,
   0b00011000,
   0b00011000,
   0b00000000,
   0b00000000,
   0b00000000};

static const unsigned char PROGMEM path_left_bmp[] =
 { 0b00000000,
   0b00000000,
   0b00000000,
   0b11111000,
   0b11111000,
   0b00000000,
   0b00000000,
   0b00000000};

static const unsigned char PROGMEM path_down_bmp[] =
 { 0b00000000,
   0b00000000,
   0b00000000,
   0b00011000,
   0b00011000,
   0b00011000,
   0b00011000,
   0b00011000};

static const unsigned char PROGMEM path_right_bmp[] =
 { 0b00000000,
   0b00000000,
   0b00000000,
   0b00011111,
   0b00011111,
   0b00000000,
   0b00000000,
   0b00000000};
  
static const unsigned char PROGMEM explosion_1_bmp[] =
 { 0b00000000,
   0b00000000,
   0b00000000,
   0b00011000,
   0b00011000,
   0b00000000,
   0b00000000,
   0b00000000};

static const unsigned char PROGMEM explosion_2_bmp[] =
 { 0b00000000,
   0b01000010,
   0b00100100,
   0b00000000,
   0b00000000,
   0b00100100,
   0b01000010,
   0b00000000};

static const unsigned char PROGMEM explosion_3_bmp[] =
 { 0b11000011,
   0b11100111,
   0b01100110,
   0b00000000,
   0b00000000,
   0b01100110,
   0b11100111,
   0b11000011};


char start = 0;
char bike_x = (SCREEN_WIDTH/TILE_SIZE)/2;
char bike_y = (SCREEN_HEIGHT/TILE_SIZE)/2;
char bike_dir = 3;
char n_pos = 0;
char pos_list[(SCREEN_WIDTH/TILE_SIZE)*(SCREEN_HEIGHT/TILE_SIZE)][2];


void setup() {
  Serial.begin(9600);

  pinMode(2, INPUT);
  digitalWrite(2, LOW);

  if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed"));
    for(;;);
  }

}

void loop() {
  display_func();
  input();
  move_bike();
}

void input() {
  int i;
  for (i = 0; i < 20; i++) {
    char direction = 5;
    int in_x = analogRead(0);
    int in_y = analogRead(1);
    if (in_y > 750) direction = 0;
    if (in_x < 250) direction = 1;
    if (in_y < 250) direction = 2;
    if (in_x > 750) direction = 3;
    if (start == 0 && direction != 5) {bike_dir = direction; start = 1;}
    else if (abs(direction - bike_dir) != 2 && direction != 5) bike_dir = direction;
    delay(25);
  } 
}

void move_bike() {
  if (start == 1) {
    pos_list[n_pos][0] = bike_x; pos_list[n_pos][1] = bike_y;
    n_pos++;
    if (bike_dir == 0) bike_y -= 1;
    else if (bike_dir == 1) bike_x -= 1;
    else if (bike_dir == 2) bike_y += 1;
    else if (bike_dir == 3) bike_x += 1;
    if (check_collision())
      game_end();
  }
}

void game_end() {
  display.clearDisplay();
  draw_path(1);
  display.drawBitmap(pos_list[n_pos - 1][0] * TILE_SIZE, pos_list[n_pos - 1][1] * TILE_SIZE, explosion_1_bmp, TILE_SIZE, TILE_SIZE, SSD1306_WHITE);
  display.display();
  delay(500);
  display.clearDisplay();
  draw_path(1);
  display.drawBitmap(pos_list[n_pos - 1][0] * TILE_SIZE, pos_list[n_pos - 1][1] * TILE_SIZE, explosion_2_bmp, TILE_SIZE, TILE_SIZE, SSD1306_WHITE);
  display.display();
  delay(500);
  display.clearDisplay();
  draw_path(1);
  display.drawBitmap(pos_list[n_pos - 1][0] * TILE_SIZE, pos_list[n_pos - 1][1] * TILE_SIZE, explosion_3_bmp, TILE_SIZE, TILE_SIZE, SSD1306_WHITE);
  display.display();
  delay(500);
  display.clearDisplay();
  draw_path(1);
  display.display();
  delay(1000);
  display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(WHITE);
  display.setCursor(0, 0);
  display.println(F("Points:"));
  display.println(n_pos-1, DEC);
  display.display();
  for (;;);
}

void game_reset() {
  start = 0;
  bike_x = (SCREEN_WIDTH/TILE_SIZE)/2;
  bike_y = (SCREEN_HEIGHT/TILE_SIZE)/2;
  bike_dir = 3;
  n_pos = 0;
}

char check_collision() {
  int i;
  for (i = 0; i < n_pos; i++)
    if (pos_list[i][0] == bike_x && pos_list[i][1] == bike_y) return 1;
  if (bike_x < 0 || bike_x >= SCREEN_WIDTH/TILE_SIZE) return 1;
  if (bike_y < 0 || bike_y >= SCREEN_HEIGHT/TILE_SIZE) return 1;
  return 0;
}

void display_bike() {
  const unsigned char *bitmap;
  if (bike_dir == 0) bitmap = bike_up_bmp;
  else if (bike_dir == 1) bitmap = bike_left_bmp;
  else if (bike_dir == 2) bitmap = bike_down_bmp;
  else if (bike_dir == 3) bitmap = bike_right_bmp;
  display.drawBitmap(bike_x * TILE_SIZE, bike_y * TILE_SIZE, bitmap, TILE_SIZE, TILE_SIZE, SSD1306_WHITE);
}

void draw_path(char doTheThing) {
  const unsigned char *bitmap;
  int i;
  for (i = 0; i < n_pos; i++) {
    if (i > 0 && !(i == n_pos-1 && doTheThing == 1)) {
      if (pos_list[i-1][1] < pos_list[i][1]) bitmap = path_up_bmp;
      else if (pos_list[i-1][0] < pos_list[i][0]) bitmap = path_left_bmp;
      else if (pos_list[i-1][1] > pos_list[i][1]) bitmap = path_down_bmp;
      else if (pos_list[i-1][0] > pos_list[i][0]) bitmap = path_right_bmp;
      display.drawBitmap(pos_list[i][0] * TILE_SIZE, pos_list[i][1] * TILE_SIZE, bitmap, TILE_SIZE, TILE_SIZE, SSD1306_WHITE);
    }
    if (i < n_pos-1) {
      if (pos_list[i+1][1] < pos_list[i][1]) bitmap = path_up_bmp;
      else if (pos_list[i+1][0] < pos_list[i][0]) bitmap = path_left_bmp;
      else if (pos_list[i+1][1] > pos_list[i][1]) bitmap = path_down_bmp;
      else if (pos_list[i+1][0] > pos_list[i][0]) bitmap = path_right_bmp;
      display.drawBitmap(pos_list[i][0] * TILE_SIZE, pos_list[i][1] * TILE_SIZE, bitmap, TILE_SIZE, TILE_SIZE, SSD1306_WHITE);   
    } else if (doTheThing != 1) {
      if (bike_y < pos_list[i][1]) bitmap = path_up_bmp;
      else if (bike_x < pos_list[i][0]) bitmap = path_left_bmp;
      else if (bike_y > pos_list[i][1]) bitmap = path_down_bmp;
      else if (bike_x > pos_list[i][0]) bitmap = path_right_bmp;
      display.drawBitmap(pos_list[i][0] * TILE_SIZE, pos_list[i][1] * TILE_SIZE, bitmap, TILE_SIZE, TILE_SIZE, SSD1306_WHITE);      
    }
  }
}

void display_func() {
  display.clearDisplay();
  display_bike();
  draw_path(0);
  display.display();
}

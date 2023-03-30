#include "LedControl.h"

struct Pins {
  static const short CLK = 10;
  static const short CS = 11;
  static const short DIN = 12;

  static const short reost = A7;

  static const short joystickX = A2;
  static const short joystickY = A3;
  static const short joystickVCC = 15;
  static const short joystickGND = 14;
};

void setup() {
  startup();
}

void loop() {
  spawnFood();
  inputs();
  snakeMovement();
  system();  
}

LedControl matrix(Pins::DIN, Pins::CLK, Pins::CS, 1);

struct Point {
  int row = 0, col = 0;
  Point(int row =0, int col = 0): row(row), col(col) {};
};

struct Coordinate {
  int x = 0, y = 0;
  Coordinate(int x = 0, int y = 0): x(x), y(y) {};
};

bool gameOver = false;

Point snake;
Point food(-1,-1);

Coordinate joystickDef(500, 500);

int snakeLength = 3;
int snakeSpeed = 1;
int snakeMove = 0;

const short plusY = 1;
const short minusY = 3;
const short plusX = 2;
const short minusX = 4;

const int joystickThreshold = 160;

const float logarithmy = 0.3;

int board[8][8] = {};

void spawnFood(){
  if (food.row == -1 || food.col == -1){
    do{
      food.col = random(8);
      food.row = random(8);
    } while (board[food.row][food.col] > 0);
  } 
}
void inputs(){
  int prevDirection = snakeMove;
  long time = millis();

  while (millis() < time + snakeSpeed){
    float raw = mapf(analogRead(Pins::reost), 0, 1023, 0, 1);
		snakeSpeed = mapf(pow(raw, 3.5), 0, 1, 10, 1000);

    if (snakeSpeed == 0) {
      snakeSpeed = 1;
    }

    if (analogRead(Pins::joystickY) < joystickDef.y - joystickThreshold) {
      snakeMove = minusY;
    }
    if (analogRead(Pins::joystickY) > joystickDef.y + joystickThreshold) {
      snakeMove = plusY;
    }
    if (analogRead(Pins::joystickX) < joystickDef.x - joystickThreshold) {
     snakeMove = plusX;
    }
    if (analogRead(Pins::joystickX) > joystickDef.x + joystickThreshold) {
      snakeMove = minusX;
    }

    if (snakeMove + 2 == prevDirection && prevDirection != 0) {
      snakeMove = prevDirection;
    }
    if (snakeMove - 2 == prevDirection && prevDirection != 0) {
      snakeMove = prevDirection;
    }
    matrix.setLed(0, food.row, food.col, 1);
  }
}

void snakeMovement(){
  switch (snakeMove){
    case plusY:
      snake.row--;
      edge();
      matrix.setLed(0, snake.row, snake.col, 1);
      break;

    case minusY:
      snake.row++;
      edge();
      matrix.setLed(0, snake.row, snake.col, 1);
      break;

    case plusX:
      snake.col++;
      edge();
      matrix.setLed(0, snake.row, snake.col, 1);
      break;

    case minusX:
      snake.col--;
      edge();
      matrix.setLed(0, snake.row, snake.col, 1);
      break;
  }

  if (board[snake.row][snake.col] > 1 && snakeMove != 0){
    gameOver = true;
    return;
  }

  if (snake.row == food.row && snake.col == food.col) {
		food.row = -1; 
		food.col = -1;

    snakeLength ++;

    for (int row = 0; row < 8; row++){
      for (int col = 0; col < 8; col++){
        if (board[row][col] > 0) {
          board[row][col]++;
        }
      }
    }
  }
  
  board[snake.row][snake.col] = snakeLength + 1;

  for (int row = 0; row < 8; row++){
    for (int col = 0; col < 8; col++){
      if (board[row][col] > 0){
        board[row][col]--;
      }
      matrix.setLed(0, row, col, board[row][col] == 0 ? 0:1);
    }
  }
}

void edge(){
  if (snake.col < 0) {
    snake.col += 8;
  }
  if (snake.col > 7) {
    snake.col -= 8;
  }
  if (snake.row < 0) {
    snake.row += 8;
  }
  if (snake.row > 7) {
    snake.row -= 8;
  }
}

void system(){
  if (gameOver){
    gameOver = false;
    snake.row = random(8);
    snake.col = random(8);
    food.row = -1;
    food.col = -1;
    snakeLength = 3;
    snakeMove = 0;
    matrix.clearDisplay(0);
  }
}

void startup(){
  pinMode(Pins::joystickVCC, OUTPUT);
  digitalWrite(Pins::joystickVCC, HIGH);

  pinMode(Pins::joystickGND, OUTPUT);
  digitalWrite(Pins::joystickGND, LOW);

  matrix.shutdown(0, false);
  matrix.setIntensity(0, 8);
  matrix.clearDisplay(0);

  randomSeed(analogRead(A5));
  snake.row = random(8);
  snake.col = random(8);
}

float mapf(float x, float in_min, float in_max, float out_min, float out_max) {
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}

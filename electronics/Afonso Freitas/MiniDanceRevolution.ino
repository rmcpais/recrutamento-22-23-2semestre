//YWROBOT
//Compatible with the Arduino IDE 1.0
//imported from LiquidCrystal I2C by Frank de Brabander

#include <Wire.h>
#include <limits.h>
#include <LiquidCrystal_I2C.h>

//this project is simple so we are using global varaibles everywhere c:

#if defined(ARDUINO) && ARDUINO >= 100
#define printByte(args)  write(args);
#else
#define printByte(args)  print(args,BYTE);
#endif

#define LCD_LINE_SIZE 16
#define SCORE_LIMIT 99999

#define EMPTY_CHAR 4
#define LEFT_ARROW 3
#define RIGHT_ARROW 2
#define UP_ARROW 1
#define DOWN_ARROW 0

uint8_t gameDisplay[LCD_LINE_SIZE] = {};

//there is a better way to represent this but now its done
byte fullHealth[] = {
  0b11111,
  0b11111,
  0b11111,
  0b11111,
  0b11111,
  0b11111,
  0b11111,
  0b11111
};

byte seveneightyHealth[] = {
  0b00000,
  0b11111,
  0b11111,
  0b11111,
  0b11111,
  0b11111,
  0b11111,
  0b11111
};

byte threequartHealth[] = {
  0b00000,
  0b00000,
  0b11111,
  0b11111,
  0b11111,
  0b11111,
  0b11111,
  0b11111
};

byte fiveeightyHealth[] = {
  0b00000,
  0b00000,
  0b00000,
  0b11111,
  0b11111,
  0b11111,
  0b11111,
  0b11111
};

byte halfHealth[] = {
  0b00000,
  0b00000,
  0b00000,
  0b00000,
  0b11111,
  0b11111,
  0b11111,
  0b11111
};


byte threeeightyHealth[] = {
  0b00000,
  0b00000,
  0b00000,
  0b00000,
  0b00000,
  0b11111,
  0b11111,
  0b11111
};



byte onequartHealth[] = {
  0b00000,
  0b00000,
  0b00000,
  0b00000,
  0b00000,
  0b00000,
  0b11111,
  0b11111
};



byte oneeightyHealth[] = {
  0b00000,
  0b00000,
  0b00000,
  0b00000,
  0b00000,
  0b00000,
  0b00000,
  0b11111
};


byte noHealth[] = {
  0b00000,
  0b00000,
  0b00000,
  0b00000,
  0b00000,
  0b00000,
  0b00000,
  0b00000
};

byte emptyChar[] = {
  B00000,
  B00000,
  B00000,
  B00000,
  B00000,
  B00000,
  B00000,
  B00000
};

byte arrowDown[] = {
  B00000,
  B00100,
  B00100,
  B10101,
  B01110,
  B00100,
  B00000,
  B00000
};

byte arrowLeft[] = {
  B00000,
  B00100,
  B01000,
  B11111,
  B01000,
  B00100,
  B00000,
  B00000
};


byte arrowRight[] = {
  B00000,
  B00100,
  B00010,
  B11111,
  B00010,
  B00100,
  B00000,
  B00000
};

byte arrowUp[] = {
  B00000,
  B00100,
  B01110,
  B10101,
  B00100,
  B00100,
  B00000,
  B00000
};

const int SW_pin = 2;
const int X_pin = 0;
const int Y_pin = 1;
int VRx = 0;
int VRy = 0;
bool used = false;
bool flag = true;
int opperation = 0;
long int score = 0;
int health = 8;
int randomNumber;

unsigned long previousMillis = 0;
unsigned long currentMillis = millis();
  
LiquidCrystal_I2C lcd(0x3F,16,2);

void resetGameDisplay(){
  for(int i = 0; i < LCD_LINE_SIZE; i++){
    gameDisplay[i] = EMPTY_CHAR;
  } 
}

void setup()
{
  pinMode(SW_pin, INPUT);
  digitalWrite(SW_pin, HIGH);
  Serial.begin(9600); //
  lcd.init();                      // initialize the lcd 
  lcd.backlight();
  
  lcd.createChar(DOWN_ARROW, arrowDown);
  lcd.createChar(UP_ARROW, arrowUp);
  lcd.createChar(LEFT_ARROW, arrowLeft);
  lcd.createChar(RIGHT_ARROW, arrowRight);
  lcd.createChar(EMPTY_CHAR, emptyChar);
  lcd.createChar(5, fullHealth);
  lcd.home();
  
}

void showHealth(){
  switch(health) {
  case 0:
    lcd.createChar(5, noHealth);
    break;
  case 1:
    lcd.createChar(5, oneeightyHealth);
    break;
  case 2:
    lcd.createChar(5, onequartHealth);
    break;
  case 3:
    lcd.createChar(5, threeeightyHealth);
    break;
  case 4:
    lcd.createChar(5, halfHealth);
    break;
  case 5:
    lcd.createChar(5, fiveeightyHealth);
    break;
  case 6:
    lcd.createChar(5, threequartHealth);
    break;
  case 7:
    lcd.createChar(5, seveneightyHealth);
    break;
  case 8:
    lcd.createChar(5, fullHealth);
    break;
  default:
    lcd.createChar(5, fullHealth);
  }
  lcd.setCursor(LCD_LINE_SIZE - 1,0);
  lcd.printByte(5);
}

void verifyJoystickRotation(){
  lcd.setCursor(0, 0);
  lcd.print("Hold ");
  lcd.printByte(UP_ARROW);
  lcd.print(" For 3 sec");
  lcd.setCursor(0, 1);
  lcd.print("To start!");
  while(currentMillis - previousMillis < 3000){
    currentMillis = millis();
    getOpperation();
    lcd.setCursor(10, 1);
    lcd.printByte(opperation);
    if(opperation != UP_ARROW){
      previousMillis = currentMillis;
    }
  }

}

void getOpperation(){
  VRy = analogRead(Y_pin);
  VRx = analogRead(X_pin);
  if(VRy> 800){
    used = true;
    opperation = DOWN_ARROW;
  }  
  else if(VRy < 300){
    used = true;
    opperation = UP_ARROW;
  }else if(VRx > 800){
    used = true;
    opperation = RIGHT_ARROW;
  } else if(VRx < 300){
    used = true;
    opperation = LEFT_ARROW;
  } else{
    opperation = EMPTY_CHAR;
  }

}

void cleanGame(){
  lcd.setCursor(0,0);
  for(int i = 0; i < 10; i++){
    lcd.printByte(EMPTY_CHAR);
  }
  lcd.setCursor(0,1);
  for(int i = 0;i < LCD_LINE_SIZE; i++){
    lcd.printByte(EMPTY_CHAR);
  }
}

bool verifyLastCol(){
  return gameDisplay[LCD_LINE_SIZE - 1] == opperation; 
}

void shiftArray(){
  randomNumber = random(0,12);
  randomNumber = min(randomNumber, 4);
  for(int i = LCD_LINE_SIZE - 1; i > 0; i-- ){
    gameDisplay[i] = gameDisplay[i - 1];
  }
  gameDisplay[0] = randomNumber;
}

void waitForGameStart(){
  used = false;
  opperation = 0;
  score = 0;
  health = 8;
  opperation = EMPTY_CHAR;
  resetGameDisplay();
  lcd.clear();
  lcd.print("Run Starts In:");
  lcd.setCursor(15, 0);
  lcd.printByte(DOWN_ARROW);
  lcd.setCursor(14,1);
  lcd.printByte(RIGHT_ARROW);

  lcd.setCursor(0, 1);
  lcd.print("3 ");
  delay(1000);
  lcd.print("2 ");
  delay(1000);
  lcd.print("1 ");
  delay(1000);

}

void handleResult(){
  if(verifyLastCol()){
    lcd.setCursor(0, 0);
    if(gameDisplay[15] != EMPTY_CHAR){
      lcd.print("NICE");
      score += 50;
      lcd.printByte(opperation);
      lcd.setCursor(10, 0);
      lcd.print(score);
    }
  } else {
    lcd.setCursor(0, 0);
    lcd.print("NOT NICE");
    lcd.printByte(opperation);
    health--;
    showHealth();
  }
}

// Run the game
void runGame(void) {
  lcd.clear();
  currentMillis = millis();
  previousMillis = currentMillis;
  lcd.setCursor(10, 0);
  lcd.print(score);
  showHealth();
  while (score < SCORE_LIMIT && health > 0) {
    currentMillis = millis();
    if(currentMillis - previousMillis >= 500 && flag == true){
      previousMillis += 500;
      cleanGame();
      flag = false;
    }
    if(currentMillis - previousMillis >= 200 && flag == false){
      previousMillis += 200;
      handleResult();
      shiftArray();
      lcd.setCursor(0, 1);
      for( int i = 0; i < LCD_LINE_SIZE; i++){
        lcd.printByte(gameDisplay[i]);
      }
      used = false;
      flag = true;
    }
    if(used == false){
      getOpperation();
    }
  }
}

//Show Game Result
void waitForReset(){
  lcd.clear();
  lcd.setCursor(0,0);
  if( score > SCORE_LIMIT){
    lcd.print("CONGRATS U WON!");
  } else {
    lcd.print("CONGRATS U LOST!");
  }
  lcd.setCursor(0,1);
  //lcd.print("Press J3 Restart");
  lcd.print("Score: ");
  lcd.print(score);
  /*int buttonState = LOW;
  while(buttonState != HIGH){
    buttonState = digitalRead(SW_pin);
  }*/ //supposed to work if Switch Conection
  delay(5000);
  lcd.clear();
}

void loop()
{ 
  verifyJoystickRotation();
  waitForGameStart();
  runGame();
  waitForReset();
}


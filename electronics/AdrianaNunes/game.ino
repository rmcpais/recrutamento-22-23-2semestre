/* 
- O objetivo do jogo e clicar no botao quando a cor certa (a que aparecer no LED RGB) ligar:
  -> Cada vez que se acerta, ganha-se um ponto e a velocidade aumenta;
  -> Em caso de erro, perde-se uma vida. Pode-se falhar, no maximo, 3 vezes (na 4a o jogo acaba).
*/

#define BUTTON 2

#define RED_LED 9
#define GREEN_LED 11
#define BLUE_LED 10
#define YELLOW_LED 12

#define RGB_RED_LED 8
#define RGB_GREEN_LED 7
#define RGB_BLUE_LED 6

#define MAX_TRIES 3

#define debounce 1


typedef enum {
  NO_COLOR = -1,
  RED = 0,
  GREEN = 1,
  BLUE = 2,
  YELLOW = 3,
  WHITE = 4
} colors;

unsigned long lightRate = 2000;
int fails = 0;
int score = 0;
volatile int rightColor = NO_COLOR;
volatile int currentColor = NO_COLOR;
volatile int previousColor = NO_COLOR;
bool running = false;
int elapse_timer = 0;

static int leds[] = {RED_LED, GREEN_LED, BLUE_LED, YELLOW_LED};

void setup() {

  Serial.begin(9600);
  
  pinMode(BUTTON, INPUT_PULLUP);
  
  pinMode(RED_LED, OUTPUT);
  pinMode(GREEN_LED, OUTPUT);
  pinMode(BLUE_LED, OUTPUT);
  pinMode(YELLOW_LED, OUTPUT);
  
  pinMode(RGB_RED_LED, OUTPUT);
  pinMode(RGB_GREEN_LED, OUTPUT);
  pinMode(RGB_BLUE_LED, OUTPUT);

  attachInterrupt(digitalPinToInterrupt(BUTTON), pressButton, FALLING);

  randomSeed(analogRead(0));
  running = true;
}

void loop() {

  Serial.print("Novo jogo. ");
  chooseColor();
  
  while (fails <= MAX_TRIES) {
    currentColor = random(RED, YELLOW+1);
    digitalWrite(leds[currentColor], HIGH);

    delay(lightRate);

    digitalWrite(leds[currentColor], LOW);
    currentColor = NO_COLOR;
    
    delay(random(2000));
  }

  while (running == false) {
    Serial.println("=== Clica para voltar a jogar. ===\n");
    blink();
  }

}

void blink() {
    // color code #FFFFFF (R = 255, G = 255, B = 255)
    analogWrite(RGB_RED_LED,   255);
    analogWrite(RGB_GREEN_LED, 255);
    analogWrite(RGB_BLUE_LED,  255);
    delay(1000);

    // color code #000000 (R = 0, G = 0, B = 0)
    analogWrite(RGB_RED_LED,   0);
    analogWrite(RGB_GREEN_LED, 0);
    analogWrite(RGB_BLUE_LED,  0);
    delay(1000);
}

void chooseColor() {
  rightColor = random(RED, YELLOW+1);
    switch(rightColor) {
      case RED:
        // color code #FF0000 (R = 255, G = 0, B = 0)
        analogWrite(RGB_RED_LED,   255);
        analogWrite(RGB_GREEN_LED, 0);
        analogWrite(RGB_BLUE_LED,  0);
        Serial.println("A cor atual é VERMELHO.\n");
        break;
        
      case GREEN:
        // color code #00FF00 (R = 0, G = 255, B = 0)
        analogWrite(RGB_RED_LED,   0);
        analogWrite(RGB_GREEN_LED, 255);
        analogWrite(RGB_BLUE_LED,  0);
        Serial.println("A cor atual é VERDE.\n");
        break;
        
      case BLUE:
        // color code #0000FF (R = 0, G = 0, B = 255)
        analogWrite(RGB_RED_LED,   0);
        analogWrite(RGB_GREEN_LED, 0);
        analogWrite(RGB_BLUE_LED,  255);
        Serial.println("A cor atual é AZUL.\n");
        break;
        
      case YELLOW:
        // color code #FFFF00 (R = 255, G = 255, B = 0)
        analogWrite(RGB_RED_LED,   255);
        analogWrite(RGB_GREEN_LED, 255);
        analogWrite(RGB_BLUE_LED,  0);
        Serial.println("A cor atual é AMARELO.\n");
        break;
        
    }   
}

void pressButton() {
  noInterrupts();
  static unsigned long last_interrupt_time = 0;
  unsigned long interrupt_time = millis();

  if (interrupt_time - last_interrupt_time > 200) {
    if (running) {
      if (currentColor == rightColor) {
        // acertou
        score += 1;
        Serial.print("** Boa! Acertaste na cor certa! Tens ");
        Serial.print(score);
        Serial.println(" ponto(s). **\n");
        lightRate *= 0.95;
        chooseColor();
        
      } else {
        // errou
        fails += 1;
        if (fails <= 3) {
          // ainda existem tentativas
          Serial.print("** Falhaste, podes errar mais ");
          Serial.print(MAX_TRIES - fails);
          Serial.println(" vez(es). **\n");
          chooseColor();
          
        } else {
          // ja nao existem tentativas
          running = false;
          Serial.print("=== Fim do jogo, ficaste com ");
          Serial.print(score);
          Serial.println(" ponto(s). ===\n");
          
        }
        
      }
    } else {
      // recomecar jogo
      running = true;
      fails = 0;
      lightRate = 2000;
      score = 0;
      
    }
    
  }
  last_interrupt_time = interrupt_time;

  interrupts();
  
}

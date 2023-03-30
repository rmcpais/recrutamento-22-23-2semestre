//Library for Controling the lock using an IR reciever
#include <IRremote.h> 

#define IR_RECEIVE_PIN 4
#define LOCKED_LED_PIN 2
#define RECEIVING_LED_PIN 8
#define RELAY_CONTROL 10 

/*
    The code for unlocking the lock can be any combination of numbers ranging in [0, 9]
    Therofore, to define a pass code all you have to do is, insert the sequence of CHARS (!)
    int the array bellow
*/
char pass_code[] = {'1', '7'};

//Declaration of useful global variables
const int pass_size = sizeof(pass_code);
char cod_arr[pass_size];
int i = 0;
int locked = 1;
char code;

/*
    The IR reciever returns integer values based on the signals it detects, those values can be decoded into
    specific chars (or anything really), if you know the codification of your IR transmitter

        Args: int code -> Integer detected by the IR reciever

        Returns Values: char -> Respective char translation
*/
char decode(int code){
  switch(code){
    case 22: 
    return '0';
    case 12: 
    return '1';
    case 24: 
    return '2';
    case 94: 
    return '3';
    case 8: 
    return '4';
    case 28: 
    return '5';
    case 90: 
    return '6';
    case 66: 
    return '7';
    case 82: 
    return '8';
    case 74: 
    return '9';
    default:
    return 'N';
  }
}

/*
    This function is used to run through the array of inserted numbers (chars)
    to determine if that inserted code equals the pass code

        Args: char *code_inserted -> Array of chars containing the code that the user typed

        Return Values: int -> 1 if it's the right code / 0 -> else
*/
int verify(char *code_inserted){
  int aux = 0;
  for(int n = 0; n<pass_size; n++){
    if(code_inserted[n] == pass_code[n]){
      aux += 1;
    }
  }
  if(aux==pass_size) return 1;
  return 0;
}

//Setup, initiates the reciever and the LED pins
void setup() {
  IrReceiver.begin(IR_RECEIVE_PIN);
  pinMode(LOCKED_LED_PIN, OUTPUT);
  pinMode(RECEIVING_LED_PIN, OUTPUT);
  pinMode(RELAY_CONTROL, OUTPUT);
}

//In the first iteration the system starts as locked!
void loop() {
  if(locked){
    //Set LOCKED_LED to ON
    digitalWrite(LOCKED_LED_PIN,HIGH);
    //Activates the lock
    digitalWrite(RELAY_CONTROL,HIGH);

    //If recieved anything
    if (IrReceiver.decode()) {
        //Set sensor led to one, to show that something is being detected and decodes the message
        digitalWrite(RECEIVING_LED_PIN,HIGH);
        IrReceiver.resume();
        code = decode(IrReceiver.decodedIRData.command);
        //If a not translatable code is detected, restarts the counting of the index
        if(code == 'N'){
            i = 0;
        }else{
            //Else, fills the input array in said code and increments it's write index
            cod_arr[i] = code;
            i += 1;
        }
        delay(300);
        digitalWrite(RECEIVING_LED_PIN,LOW);
    }
    //In case that we have reached the end of the input index we submmit said input
    //to be verified, if 1 is returned, the system unlocks (setting locked to 0) 
    if(i >= pass_size){
        if(verify(cod_arr)){
        locked = 0;
        }
        i = 0;
    }
  }else{
    //When the system is unlocked, locked LED turns OFF
    digitalWrite(LOCKED_LED_PIN,LOW);
    //and the lock is deactivatted
    digitalWrite(RELAY_CONTROL,LOW);

    if (IrReceiver.decode()) {
        //Sames process as before, only now we detect if the user sent a '5' which locks the system
        digitalWrite(RECEIVING_LED_PIN,HIGH);
        IrReceiver.resume();
        code = decode(IrReceiver.decodedIRData.command);
        if(code == '5') locked = 1;
        delay(300);
        digitalWrite(RECEIVING_LED_PIN,LOW);
    }
  }
}
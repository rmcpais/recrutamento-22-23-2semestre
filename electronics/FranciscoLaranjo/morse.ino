//projeto visto online
//https://wokwi.com/projects/360185483038785537
// consiste num tradutor de morse code

int buzzer = 6;
int led = 2;

void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  pinMode(buzzer,OUTPUT);
}

String translateChar(char letra) {
  switch(letra) {
    case 'a':
        return ".-";
    case 'b':
        return "-...";
    case 'c':
        return "-.-.";
    case 'd':
        return "-..";
    case 'e':
        return ".";
    case 'f':
        return "..-.";
    case 'g':
        return "--.";
    case 'h':
        return "....";
    case 'i':
        return "..";
    case 'j':
        return ".---";
    case 'k':
        return "-.-";
    case 'l':
        return ".-..";
    case 'm':
        return "--";
    case 'n':
        return "-.";
    case 'o':
        return "---";
    case 'p':
        return ".--.";
    case 'q':
        return "--.-";
    case 'r':
        return ".-.";
    case 's':
        return "...";
    case 't':
        return "-";
    case 'u':
        return "..-";
    case 'v':
        return "...-";
    case 'w':
        return ".--";
    case 'x':
        return "-..-";
    case 'y':
        return "-.--";
    case 'z':
        return "--..";
    case '1':
        return ".----";
    case '2':
        return "..---";
    case '3':
        return "...--";
    case '4':
        return "....-";
    case '5':
        return ".....";
    case '6':
        return "-....";
    case '7':
        return "--...";
    case '8':
        return "---..";
    case '9':
        return "----.";
    case '0':
        return "-----";
    case ' ':
        return "/";
    default:
        return "";
    }
}

String translateString(String frase){
    String fraseTraduzida = "";
    for(char letra : frase){
        fraseTraduzida = fraseTraduzida + " " + translateChar(letra);
    }
    return fraseTraduzida;
}

void emitirSom(char morseChar){
    if (morseChar == '.'){
        digitalWrite(led, HIGH);
        tone(buzzer,550);
        delay(100);
        digitalWrite(led, LOW);
        noTone(buzzer);
        delay(100);
    }else if (morseChar == '-'){
        digitalWrite(led, HIGH);
        tone(buzzer,550);
        delay(300);
      	digitalWrite(led, LOW);
        noTone(buzzer);
        delay(200);
    }else if (morseChar == ' '){
        delay(300);
    }else if (morseChar == '/'){
        delay(700);
    }
}

void loop() {
  // put your main code here, to run repeatedly:
  String morseString = translateString("sos");

  for(char l : morseString){
        emitirSom(l);
  }
  
  delay(30000);
}

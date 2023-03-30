// Defino pins

const int trigPin = 5;
const int buzzer = 3;
const int redPin = 9; 
const int greenPin = 10;
const int bluePin = 11;
const int echoPin = 6;

// Defino vaariaveis pra calculo distancia
long duration;
int distance;
int safetyDistance;


void setup() {
    
    pinMode(trigPin, OUTPUT); // trigPin como Output
    pinMode(echoPin, INPUT); // echoPin como Input
    pinMode(buzzer, OUTPUT); // buzzer como Input
    // Pins RGB
    pinMode(redPin, OUTPUT);
    pinMode(bluePin, OUTPUT);
    pinMode(redPin, OUTPUT);
    Serial.begin(9600); 

}


void loop() {
    // Reset trigpin
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);

    // trigPin em HIGH  por 10 microsec
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    // Duracao percurso
    duration = pulseIn(echoPin, HIGH);

    // Distancia calculo
    distance= duration*0.034/2;

    safetyDistance = distance;
    if (safetyDistance <= 10){
      // Setup cores e som - VERMELHO
      digitalWrite(buzzer, HIGH);
      analogWrite(redPin, 200);
      analogWrite(greenPin, 1);
      analogWrite(bluePin, 1);
      // Serial print
      Serial.print("PERIGO!!!! Obstáculo a ");
      Serial.print(safetyDistance);
      Serial.println(" metros");

    }
    if (10 < safetyDistance && safetyDistance <= 20) {
      // Setup cores e som - AMARELO
      digitalWrite(buzzer, LOW);
      analogWrite(redPin, 255);
      analogWrite(bluePin, 1);
      analogWrite(greenPin, 55);
      // Serial print
      Serial.print("Cuidado! Obstáculo a ");
      Serial.print(safetyDistance);
      Serial.println(" metros");
    }
    if (safetyDistance > 20) {
      // Setup cores e som - VERDE
      digitalWrite(buzzer, LOW);
      analogWrite(redPin, 50);
      analogWrite(greenPin, 50);
      analogWrite(bluePin, 0);
      // Serial print
      Serial.print("Obstáculo a ");
      Serial.print(safetyDistance);
      Serial.println(" metros , uma distância segura");
      
    }

  
    
}

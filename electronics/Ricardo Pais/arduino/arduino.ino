/***********************************************************
*Programa para ativar algo utilizando uma combinacao que recebe em infravermelhos
*O programa tambem controla um emissor de infravermelhos (eu não sabia se podia fazer varios sketches)
************************************************************/


#include <IRremote.h>
#include <EEPROM.h>

//definir os pinos
#define Pin_rep 8
#define Led_ir 6
#define Pin_rec 11
#define Pin_but0 12
#define Pin_but1 10
#define Pin_ver 2
#define Pin_enc 4

#define C_tam 5  //tamanho do codigo

IRrecv recv(Pin_rec);

//iniciar variaveis nessessárias ao programa
int codigo_estado = 0;
int repro_estado = 0;

//inicializar o codigo com o tamanho definido
int codigo[C_tam];


//funcao para ler um numero inteiro
int ler_int(int endreco) {
  byte byte1 = EEPROM.read(endreco);
  byte byte2 = EEPROM.read(endreco + 1);
  int res = (byte1 << 8) + byte2;
  return res;
}

//Guarda um numero inteiro na EEPROM caso o numero presente seja diferente
void guardar_int(int endreco, int n) {
  byte byte1 = (n >> 8) & 0xFF;
  byte byte2 = n & 0xFF;

  EEPROM.update(endreco, byte1);
  EEPROM.update(endreco + 1, byte2);
}


//funcao para guardar o codigo na EEPROM
void guardar_cod(int endreco) {
  for (int n = 0; n < C_tam; n++) {
    guardar_int(endreco + (2 * n), codigo[n]);
  }
}




void setup() {
  pinMode(Pin_ver, OUTPUT);
  pinMode(Pin_enc, OUTPUT);
  //botoes ativados a LOW
  pinMode(Pin_rep, INPUT_PULLUP);
  pinMode(Pin_but0, INPUT_PULLUP);
  pinMode(Pin_but1, INPUT_PULLUP);

  //inicializar o emissor e o recetor de infravermelhos
  IrSender.begin(Led_ir);
  recv.enableIRIn();

  Serial.begin(9600);

  guardar_cod(0);

  /*  dar print ao codigo guardado na EEPROM
  for(int n=0; n < C_tam; n++){
    Serial.println(ler_int(n*2));
  }
*/
}



//funcao para modificar o codigo
void repro() {
  digitalWrite(Pin_ver, HIGH);
  digitalWrite(Pin_enc, HIGH);
  codigo_estado = 0;
  //Serial.println("repro");
  while (repro_estado < C_tam) {
    comando();
    if (recv.decode()) {
      switch (recv.decodedIRData.command) {
        case 0:
          //0
          codigo[repro_estado] = 0;
          repro_estado++;
          break;
        case 1:
          //1
          codigo[repro_estado] = 1;
          repro_estado++;
          break;
      }
      digitalWrite(Pin_ver, LOW);
      delay(200);
      digitalWrite(Pin_ver, HIGH);
      recv.resume();
    }
  }
  //Serial.println("Repro Acabou");
  digitalWrite(Pin_ver, LOW);
  digitalWrite(Pin_enc, LOW);
  repro_estado = 0;
  guardar_cod(0);
  return;
}


void comb(int x) {
  if (codigo[codigo_estado] == x) {
    codigo_estado++;
  } else {  //codigo errado
    //Serial.println("bola");
    codigo_estado = 0;
    digitalWrite(Pin_enc, HIGH);
    delay(10000);
    digitalWrite(Pin_enc, LOW);
  }
  return;
}


//funcao para emitir IR
void comando() {
  if (digitalRead(Pin_but0) == LOW) {
    IrSender.sendRC5(0x0, 0x0, 13);
  } else if (digitalRead(Pin_but1) == LOW) {
    IrSender.sendRC5(0x0, 0x1, 13);
  }
  return;
}




void loop() {
  comando();

  if (digitalRead(Pin_rep) == LOW) {
    repro();
  }

  //receccao das emissoes IR
  if (recv.decode()) {
    Serial.println(recv.decodedIRData.command);
    switch (recv.decodedIRData.command) {
      case 0:
        comb(0);
        break;

      case 1:
        comb(1);
        break;
    }
    digitalWrite(Pin_enc, HIGH);
    delay(200);
    digitalWrite(Pin_enc, LOW);
    recv.resume();
  }

  if (codigo_estado >= C_tam) {   //codigo correto
    digitalWrite(Pin_ver, HIGH);  //pode ser trocado por uma funcao para fazer algo
    delay(10000);
    digitalWrite(Pin_ver, LOW);
    codigo_estado = 0;
  }
}

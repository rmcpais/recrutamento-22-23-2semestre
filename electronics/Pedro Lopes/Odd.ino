////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//         
//                                                                     What's the ODD?
//
//    O jogo é para ser jogado por 2 pessoas com “computador” como referência, e consiste em  :
//     * 3 rondas, cada jogador começa com 5 números e só pode escolher cada um, uma vez durante as 3 rondas (incluindo o computador);
//     * A cada ronda o computador tem um numero aleatório diferente entre 1 e 5 (excepto na 1º ronda em que é entre 2 e 4);
//     * Cada jogador tem que apostar um dos seus números contra o numero do computador, não sabendo o critério da ronda ou seja se o numero que aposta tem de ser menor, maior ou igual que o numero do computador;
//     * Após os 2 jogadores fazerem as suas apostas é revelado o critério e caso alguma ou ambas as apostas o cumpram ganham 1 ponto cada jogador;
//     * No final das 3 rondas aquele com mais pontos ganha;
//     * Caso haja empate existirá rondas especiais onde os jogadores podem apostar sempre qualquer número de 1 a 5, contra um numero do computador entre 2 e 4, até haver um desempate
//
//


// Variaveis
int buttonPin[2] = {2,3};
int GreenPin[5] = {12,11,10,9,8};
int RedPin[3] = {7,6,5};
int PPin[2] = {4,13};
int x,i,t;
int j[2][5] = {0}; // Numeros disponiveis para cada jogador
int c[5] = {0}; // Numeros do computador
int NC = 0; // Numero da ronda (PC)
int N[2] = {0};  // Numeros da ronda para cada jogador
int choice = 1;
int criterio = 0; // 1 - menor , 2 - igual , 3 - maior
int points[2] = {0};

void setup() {
  pinMode(buttonPin, INPUT);
  pinMode(GreenPin, OUTPUT);
  pinMode(RedPin, OUTPUT);
  pinMode(PPin, OUTPUT);
  randomSeed(analogRead(A0));
}


void loop() {
  
  for (x=0;x<5;x++);{
    digitalWrite(GreenPin[x], LOW);
  }

  for (x=0;x<3;x++);{
    digitalWrite(RedPin[x], LOW);
  }

  for (x=0;x<2;x++);{
    digitalWrite(PPin[x], LOW);
  }

 // Round 1
  delay(1500);
  NC = random(2,5);
  c[NC-1] = 1;
  digitalWrite(RedPin[1], HIGH);
  digitalWrite(GreenPin[NC-1], HIGH);
  delay(10000);
  digitalWrite(GreenPin[NC-1], LOW);
  digitalWrite(RedPin[1], LOW);
  
  apostas();
  delay(3000);
  criterio = random(1,4);
  digitalWrite(RedPin[criterio-1], HIGH);
  delay(2000);
  Points();
  delay(5000);
  digitalWrite(RedPin[criterio-1], LOW);

// Round 2 e 3
  for (int r = 0;r<2;r++){
    delay(1500);
    NC = random(1,6);
    while(c[NC-1]==1){
      NC = random(1,6);
    }
    c[NC-1] = 1;
    digitalWrite(RedPin[1], HIGH);
    digitalWrite(GreenPin[NC-1], HIGH);
    delay(10000);
    digitalWrite(GreenPin[NC-1], LOW);
    digitalWrite(RedPin[1], LOW);
    
    apostas();
    delay(3000);
    if (NC == 1){
      criterio = random(2,4);
    }
    else if (NC == 5){
      criterio = random(1,3);
    }
    else{
      criterio = random(1,4);      
    }
    digitalWrite(RedPin[criterio-1], HIGH);
    delay(2000);
    Points();
    delay(5000);
    digitalWrite(RedPin[criterio-1], LOW);   
  }
  
  // Round de desempate
  if(points[0]==points[1]){
    while(points[0]==points[1]){
      delay(1500);
      NC = random(2,5);
      digitalWrite(RedPin[1], HIGH);
      digitalWrite(GreenPin[NC-1], HIGH);
      delay(10000);
      digitalWrite(GreenPin[NC-1], LOW);
      digitalWrite(RedPin[1], LOW);
      for(int w = 0;w<2;w++){
        for(int s = 0;s<5;s++){
          j[w][s]=0;
        }
      }
      apostas();
      delay(3000);
      criterio = random(1,4);
      digitalWrite(RedPin[criterio-1], HIGH);
      delay(2000);
      Points();
      delay(5000);
      digitalWrite(RedPin[criterio-1], LOW); 
    }
  }

// Quem ganhou?
  if(points[0]>points[1]){
    Champ(0);
  }else {
    Champ(1);
  }
  
delay(100000000000000);
// O jogo acabou    

}

// apostas
 void apostas(){
  for (x=0;x<2;x++){
    digitalWrite(PPin[x], HIGH);
    for (i=0;i<5;i++){
      if(j[x][i]==1){
        continue;
      }
      digitalWrite(GreenPin[i], HIGH);
      for(t=0;t<10;t++){
        choice = digitalRead(buttonPin[x]);
        delay(300);
        if(choice == 0) {
          break;        
        }        
      }
      digitalWrite(GreenPin[i], LOW);
      if(choice == 0) {
        N[x]=i+1;
        j[x][i]=1;
          for(t=0;t<10;t++){
            digitalWrite(GreenPin[i], HIGH);
            delay(100);
            digitalWrite(GreenPin[i], LOW);
            delay(100);
          } 
          break;
      }       
    }
    choice = 0;
    digitalWrite(PPin[x], LOW);
    delay(3000);
  }
}

// quem ganhou? (Serve para cada ronda como para o jogo)

void Champ(int x){

  for(int y=0;y<10;y++){
    digitalWrite(PPin[x], HIGH);
    delay(300);  
    digitalWrite(PPin[x], LOW);
    delay(300);
  }
}



// points counter

void Points(){
  for (x=0;x<2;x++){
    switch (criterio) {
    case 1:
      if(N[x] < NC){
        points[x]++;
        Champ(x);       
      }
      break;
    case 2:
      if(N[x] == NC){
        points[x]++;
        Champ(x); 
      }
      break;
    case 3:
      if(N[x] > NC){
        points[x]++;
        Champ(x); 
      }
      break;
    }
  }
}

const int infrarrojo_1 = 25; // rojo
const int infrarrojo_2 = 26; // amarillo

int estado_anterior_1 = 1; // 0: lona, 1: aire
int estado_anterior_2 = 1; // 0: lona, 1: aire

int contador_1 = 0;
int contador_2 = 0;

unsigned long tiempo_previo = 0;
const long tiempo_espera = 5 ;


void setup() {
  pinMode(infrarrojo_1, INPUT);
  pinMode(infrarrojo_2, INPUT);
  Serial.begin(115200);

}

void loop() {
  
    if (millis() - tiempo_previo >= tiempo_espera) {
      tiempo_previo = millis(); 
    
    // trampolin 1
    if(digitalRead(infrarrojo_1) == 0 && estado_anterior_1 == 1) {
      Serial.println("aterrizo trampolin rojo");
      estado_anterior_1 = 0;
      contador_1 += 1;
      Serial.println(contador_1);
    }

    if(digitalRead(infrarrojo_1) == 1 && estado_anterior_1 == 0) {
      Serial.println("despego trampolin rojo");
      estado_anterior_1 = 1;
    }
    // trampolin 2

    if(digitalRead(infrarrojo_2) == 0 && estado_anterior_2 == 1) {
      Serial.println("aterrizo trampolin amarillo");
      estado_anterior_2 = 0;
      contador_2 += 1;
      Serial.println(contador_2);
    }

    if(digitalRead(infrarrojo_2) == 1 && estado_anterior_2 == 0) {
      Serial.println("despego trampolin amarillo");
      estado_anterior_2 = 1;
    }
    }
    
}

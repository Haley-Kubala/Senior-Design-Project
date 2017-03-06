char outString[50] = {1,1,1,1,1};
int inString = 2;
boolean PiConfirmData = false;
boolean ArduinoGotData = false;

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
}  
  /*delay(1000);
  
  Serial.println(outString);
  digitalWrite(13, HIGH);

  while (!PiConfirmData) {
    if (Serial.available()) {
      inString = Serial.read();
      if (inString == 0) {
        Serial.println(outString);
      }
      else if (inString == 1) {
        PiConfirmData = true;
      }
    }
  }
  
  delay(1000);*/
  
  /*while (!ArduinoGotData) {
    if (Serial.available()) {
      inString = Serial.read();
      ArduinoGotData = true;
    }
  }
  
  if (inString
}*/

//void loop() {}
  
void loop() {
  digitalWrite(13, HIGH);
  delay(1000);
  digitalWrite(13, LOW);
  
  Serial.println("test");
  
  /*if (Serial.available()) {
    int n = Serial.read() - '0';
    digitalWrite(13, HIGH);
    sentData = false;
  }*/
  
  delay(1000);
}

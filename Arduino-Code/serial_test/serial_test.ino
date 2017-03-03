char outString[50] = {1,1,1,1,1};
char inString[50];
boolean PiConfirmData = false;
boolean ArduinoGotData = false;

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
  
  delay(1000);
  
  Serial.println(dataString);
  digitalWrite(13, HIGH);

  while (!PiConfirmData) {
    if (Serial.available()) {
      inString = Serial.read();
      if (inString[0] == 0) {
        Serial.println(dataString);
      }
      else if (inString[0] == 1) {
        PiConfirmData = true;
      }
    }
  }
  
  /*delay(1000);
  
  while (!ArduinoGotData) {
    if (Serial.available()) {
      inString = Serial.read();
      ArduinoGotData = true;
    }
  }
  
  if (inString*/
}

void loop() {}
  
/*void loop() {
  if (!sentData) {
    a++;                          // a value increase every loop
    sprintf(dataString,"%02X",a); // convert a value to hexa
    Serial.println(dataString);   // send the data
    digitalWrite(13, LOW);
    sentData = true;
  }
  else {
    if (Serial.available()) {
      int n = Serial.read() - '0';
      digitalWrite(13, HIGH);
      sentData = false;
    }
  }
  delay(1000);
}*/

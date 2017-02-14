char dataString[50] = {0};
int a =0;
boolean sentData = false;

void setup() {
  Serial.begin(9600);              //Starting serial communication
  pinMode(13, OUTPUT);
  digitalWrite(13, HIGH);
}
  
void loop() {
  if (!sentData) {
    a++;                          // a value increase every loop
    sprintf(dataString,"%02X",a); // convert a value to hexa
    Serial.println(dataString);   // send the data
    sentData = true;
  }
  else {
    if (Serial.available()) {
      int n = Serial.read() - '0';
      digitalWrite(13, HIGH);
      sentData = false;
    }
  }
  delay(1000);                  // give the loop some break
}

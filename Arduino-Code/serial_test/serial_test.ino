char sending[50] = "Sending data...";
char test[50] = "77778";
char test2[50] = "77777";
int input;
//int a = 0; 

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
  
  delay(100);
  
  Serial.println(sending);
  
  delay(100);
  
  Serial.println(test);
  
  delay(100);
  
  Serial.println(sending);
  
  delay(100);
  
  Serial.printlnchar(test2);
  
  delay(100);
}
  
void loop() {
  if (Serial.available() > 0) {
    input = Serial.read();
    Serial.println(input);
    
    if (input == 48) { // 48 is ASCII for 0 (zero)
      digitalWrite(13, LOW);
    }
    
    if (input == 49) { // 49 is ASCII for 1 (one)
      digitalWrite(13, HIGH);
    }      
  }
  delay(100);
}

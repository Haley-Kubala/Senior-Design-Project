char sending[50] = "Sending data...";
char test[50] = "77778";
char test2[50] = "77777";
char input[50];
//int a = 0; 

void setup() {
  Serial.begin(9600);              //Starting serial communication
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
  
  delay(1000);
  
  Serial.println(sending);
  
  delay(1000);
  
  Serial.println(test);
  
  delay(1000);
  
  Serial.println(sending);
  
  delay(1000);
  
  Serial.println(test2);
  
  delay(1000);
}
  
void loop() {
  if (Serial.available() > 0) {
    input = Serial.read();
    Serial.println(input);
    
    if (input.equals("48")) { // 48 is ASCII for 0 (zero)
      digitalWrite(13, LOW);
    }
    
    if (input.equals("49")) { // 49 is ASCII for 1 (one)
      digitalWrite(13, HIGH);
    }      
  }
  delay(1000);
}

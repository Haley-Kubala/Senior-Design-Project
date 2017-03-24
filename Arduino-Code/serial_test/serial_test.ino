char sending[16] = "Sending data...";
int input; 

// test variables
char start[12] = "---start---";
char ending[12] = "----end----";
char test[6] = "77778";
char test2[6] = "77777";
int wait = 100;

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
  
  delay(wait);
  
  Serial.println(start);
  
  delay(wait);
  
  Serial.println(sending);
  
  delay(wait);
  
  Serial.println(test);
  
  delay(wait);
  
  Serial.println(sending);
  
  delay(wait);
  
  Serial.println(test2);
  
  delay(wait);
  
  Serial.println(ending);
  
  delay(wait);
  
  Serial.println("spam");
}
  
void loop() {
  if (Serial.available() > 0) {
    input = Serial.read();
    //Serial.println(input);
    
    if (input == 48) { // 48 is ASCII for 0 (zero)
      digitalWrite(13, LOW);
    }
    
    if (input == 49) { // 49 is ASCII for 1 (one)
      digitalWrite(13, HIGH);
    }      
  }
  delay(100);
}

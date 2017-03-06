char sending[50] = "Sending data...";
char test[50] = "test";
//int a = 0; 

void setup() {
  Serial.begin(9600);              //Starting serial communication
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
  
  delay(1000);
  
  Serial.println(sending);
  
  delay(1000);
  
  Serial.println(test);
  
  digitalWrite(13, HIGH);
}
  
void loop() {
  /*a++;                          // a value increase every loop
  sprintf(dataString,"%02X",a); // convert a value to hexa 
  Serial.println(dataString);   // send the data
  delay(1000);                  // give the loop some break */
}

int moistureSensor = 0;
int moistur_val;


void setup(){
  Serial.begin(9600); //open serial port
}

void loop(){
  moistur_val = analogRead(moistureSensor);
  Serial.print("moisture sensor reads ");
  Serial.println(moistur_val);
  
  delay(1000);
}

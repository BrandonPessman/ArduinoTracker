int led = 13;

void setup() {
  Serial.begin(9600);
  pinMode(led,OUTPUT);
}

void loop() {
  if (Serial.available()>0) {
    if (Serial.read() == 'R') {
      Serial.print("Arduino Ping Successful!");
      digitalWrite(led, HIGH);
      delay(500);
      digitalWrite(led, LOW);
    }
  }
}

const int ldrPin = A0;
const int led = 5;
int threshold = 700;

# baundrate = 9600  (valor standar) velocidad de comunicación

void setup()
{
  Serial.begin(9600);
  Serial.setTimeout(1);
  pinMode(ldrPin, INPUT);
  pinMode(led, OUTPUT);
}
void loop()
{
  int rawData = analogRead(ldrPin);
  Serial.println(rawData);
  if(rawData >   threshold)
  {
    digitalWrite(led, HIGH);
  }
  else
  {
    digitalWrite(led, LOW);
  }
  delay(100);
}

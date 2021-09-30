#include <LiquidCrystal_I2C.h>

#include  <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>


#define SEALEVELPRESSURE_HPA (1013.25)

Adafruit_BME280 bme; //I2C
LiquidCrystal_I2C lcd(0x27, 16, 2);
unsigned long delayTime;

void setup() {
  Serial.begin(9600);
  Serial.println(F("BME 280 test"));
  lcd.init();
  
  
  
  bool status;
    
  status = bme.begin(0x76);
  if (!status) {
    Serial.println("Could not find a valid Sensor, Check wiring!");
    while (1);
  }
  
  Serial.println( "Default TEST");
  delayTime = 30000;
  
  Serial.println();
}


void loop () {
  lcd.setCursor(0,0);
  lcd.print(bme.readTemperature());
  lcd.setCursor(0,1);
  lcd.print(bme.readHumidity());
  printValues();
  delay(delayTime);
}


void printValues() {
  Serial.print("Temperature =");
  Serial.print(bme.readTemperature());
  Serial.println("C");
  
  Serial.print ("Pressure =");
  Serial.print (bme.readPressure() /100.0F);
  Serial.println("Hpa");
  
  Serial.print("Humidity =");
  Serial.print(bme.readHumidity());
  Serial.println(" %");
  
}

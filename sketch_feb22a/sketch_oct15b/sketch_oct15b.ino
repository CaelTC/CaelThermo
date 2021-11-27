#include <LiquidCrystal_I2C.h>



LiquidCrystal_I2C lcd(0x27, 16, 2);
unsigned long delayTime;
const int A= 15;
const int B= 3;




void setup() {
  // put your setup code here, to run once:
  lcd.init();
  lcd.clear();
  lcd.backlight();

  lcd.setCursor(2,8);
  lcd.write(test());
  void test() 
    test=A+B;
}

void loop() {
  // put your main code here, to run repeatedly:

}

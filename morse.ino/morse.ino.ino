#define BLINKER_WIFI
#include <vector>
//#include <Blinker.h>
#include <Wire.h> 
#include <LiquidCrystal_I2C.h> 
#include <time.h>
#include <algorithm>//注意要包含该头文件
using namespace std;

//less than 0.5 sec:1
//more than 0.5 sec:2
int morse[200] = {12,2111,2121,211,1,1121,221,1111,11,1222,212,1211,22,21,222,1221,2212,121,111,2,112,1112,122,2112,2122,2211};
const char aToz[200] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
const int buttonPin = 0;     // the number of the pushbutton pin
const int ledPin =  2;      // the number of the LED pin
int buttonState = 0;         // variable for reading the pushbutton status
unsigned long lastMs = 0;

char auth[] = "ea9c498d5209";
char ssid[] = "PHICOMM_C4E0173_2.4G";
char pswd[] = "phi10vex00";

volatile char data;
LiquidCrystal_I2C lcd(0x27,16,2);  

int dot_or_dash(){
    if (millis() - lastMs >= 250 && millis() - lastMs < 1000)  //5S
    {
       lastMs = millis();
       return 2;
    }
    else if (millis() - lastMs <= 250)
    {
      lastMs = millis();
      return 1;
    }
    else if (millis() - lastMs >= 1000 && millis() - lastMs < 2000)
    {
      //character is over
      lastMs = millis();
      return 3;
    }
    else
    {
      //word is over
      lastMs = millis();
      return 4;
    }
    
}
void morse_code(int m)
{
  int* a = find(morse + 0,morse + 25, m);
  if (morse[a-morse] == m)
  {
  Serial.print(aToz[a-morse]); 
  lcd.print(aToz[a-morse]);
  }
}
void button1_callback(const String & state)
{
//    BLINKER_LOG("get button state: ", state);
    digitalWrite(LED_BUILTIN, !digitalRead(LED_BUILTIN));
}
void dataRead(const String & data)
{
  // BLINKER_LOG("Blinker readString: ", data);
      lcd.clear();
      lcd.setCursor(0,0);                
      lcd.print(data);     
      lcd.setCursor(0,1);
      lcd.print("       IAN");


}
void setup()
{
  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
  //Wire.begin(4,5); 
  lcd.init();                 
  lcd.backlight();   
  lcd.setCursor(0,1);
  lcd.print("        Ian");
  Serial.begin(9600);
  dot_or_dash();
  lcd.setCursor(0,0);
//  BLINKER_DEBUG.stream(Serial);
//  Blinker.begin(auth, ssid, pswd);
//  Blinker.attachData(dataRead);         
}
int last = 1;
int flag = 0;
int m = 0;
void loop()
{
 //Blinker.run();
 buttonState = digitalRead(buttonPin);
//lcd.clear();

 
  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (buttonState == HIGH ) {
    // turn LED on:
    digitalWrite(ledPin, HIGH);
     //lcd.print("High");
     if (last == 0 && flag == 1){
          int tempa=dot_or_dash();
          if (tempa != 3 && tempa != 4)
          {
            m = m * 10 + tempa;
          }
          else
          {
          //Serial.println(m);   
          morse_code(m);
          m = 0;
          if (tempa == 4)
          {
            Serial.print(" ")  ;
            lcd.print(" ");
          }
          }
          //Serial.println(dot_or_dash());     
          last = 1;
          
     }
  } else {
    // turn LED off:
    digitalWrite(ledPin, LOW);
    //lcd.print("Low ");
    if (last == 1){
      //Serial.println(dot_or_dash());     
      last = 0;
      lastMs = millis();
      flag = 1;
    }
  }
  
   //delay(1000);
   
}

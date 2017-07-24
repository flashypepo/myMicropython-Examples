   //////////////////////////////////////////////
  //   20x4 Subscriber Counter for YouTube    //
 //                                          //
//           http://www.educ8s.tv           //
/////////////////////////////////////////////

#include <Wire.h>
#include <ESP8266WiFi.h>
#include <LiquidCrystal_I2C.h>
#include <ArduinoJson.h>

byte LT[8] = 
{
  B01111,  
  B11111,  
  B11111,  
  B11111,  
  B11111,  
  B11111,  
  B11111,  
  B11111
};

byte UB[8] =
{
  B11111,  
  B11111,  
  B11111,  
  B00000,  
  B00000,  
  B00000,  
  B00000,  
  B00000
};
byte RT[8] =
{
  B11110,  
  B11111,  
  B11111,  
  B11111,  
  B11111,  
  B11111,  
  B11111,  
  B11111
};

byte LL[8] =
{
  B11111,  
  B11111,  
  B11111,  
  B11111,  
  B11111,  
  B11111,  
  B11111,  
  B01111
};

byte LB[8] =
{
  B00000,  
  B00000,  
  B00000,  
  B00000,  
  B00000,  
  B11111,  
  B11111,  
  B11111
};

byte LR[8] =
{
  B11111,  
  B11111,  
  B11111,  
  B11111,  
  B11111,  
  B11111,  
  B11111,  
  B11110
};

byte UMB[8] =
{
  B11111,  
  B11111,  
  B11111,  
  B00000,  
  B00000,  
  B00000,  
  B11111,  
  B11111
};

byte LMB[8] =
{
  B11111,  
  B00000,  
  B00000,  
  B00000,  
  B00000,  
  B11111,  
  B11111,  
  B11111
};

const char* ssid     = "SSID";       // SSID of local network
const char* password = "PASSWORD";   // Password on network
String apiKey = "YOURAPIKEY";            // YouTube Data API v3 key generated here: https://console.developers.google.com
String channelId = "UCxqx59koIGfGRRGeEm5qzjQ";   // YouTube channel id

const char *host = "www.googleapis.com";
long subscribers,subscribersBefore = 0;

LiquidCrystal_I2C lcd(0x27, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE);  // Set the LCD I2C address

void setup()  
{
  Serial.begin(9600);
  int cursorPosition=0;

  lcd.begin(20,4); 
  lcd.setCursor(0,0);
  lcd.print("Connecting ....");

  createCustomChars();
  
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    lcd.setCursor(cursorPosition,1); 
    lcd.print(".");
    cursorPosition++;
  }
  
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Connected!");
  delay(1000);
}

void loop() 
{
  int length;
  String subscribersString = String(getSubscribers());
  if(subscribers != subscribersBefore)
  {
    lcd.clear();
    length = subscribersString.length();
    printSubscribers(length,subscribersString);
    subscribersBefore = subscribers;
  }  
  delay(60000);
}

void printSubscribers(int length, String subscribersString)
{
  switch(length)
  {
    case 5: printDigits(subscribersString,5);printDigits(subscribersString,4);printDigits(subscribersString,3);printDigits(subscribersString,2);printDigits(subscribersString,1);break;
    case 4: printDigits(subscribersString,4);printDigits(subscribersString,3);printDigits(subscribersString,2);printDigits(subscribersString,1);break;
    case 3: printDigits(subscribersString,3);printDigits(subscribersString,2);printDigits(subscribersString,1);break;
    case 2: printDigits(subscribersString,2);printDigits(subscribersString,1);break;
    case 1: printDigits(subscribersString,1);break;
    default: break;
  }
}

void printDigits(String subscribersString,int digit)
{
  int length = subscribersString.length();
  char digitToPrint = subscribersString.charAt(length-digit);
  Serial.println(digitToPrint);
  switch(digit)
  {
    case 1: printDigitToScreen(digitToPrint,17); break;
    case 2: printDigitToScreen(digitToPrint,13); break;
    case 3: printDigitToScreen(digitToPrint,9); break;
    case 4: printDigitToScreen(digitToPrint,5); break;
    case 5: printDigitToScreen(digitToPrint,1); break;
  } 
}

void printDigitToScreen(char digit,int position)
{
  int digitToPrint = digit - '0'; //Convertion from char to int
  switch(digitToPrint)
  {
    case 1:digit1(position); break;
    case 2:digit2(position); break;
    case 3:digit3(position);break;
    case 4:digit4(position); break;
    case 5:digit5(position); break;
    case 6:digit6(position); break;
    case 7:digit7(position); break;
    case 8:digit8(position); break;
    case 9:digit9(position); break;    
    case 0:digit0(position); break;    
  }
}

void digit0(int position_x)
{ 
  lcd.setCursor(position_x, 1); 
  lcd.write((byte)0);  
  lcd.write(1); 
  lcd.write(2);
  lcd.setCursor(position_x, 2);
  lcd.write(3);  
  lcd.write(4);  
  lcd.write(5);
}

void digit1(int position_x) 
{
  lcd.setCursor(position_x,1);
  lcd.write(1);
  lcd.write(2);
  lcd.setCursor(position_x+1,2);
  lcd.write(5);
}

void digit2(int position_x)
{
  lcd.setCursor(position_x,1);
  lcd.write(6);
  lcd.write(6);
  lcd.write(2);
  lcd.setCursor(position_x, 2);
  lcd.write(3);
  lcd.write(7);
  lcd.write(7);
}

void digit3(int position_x)
{
  lcd.setCursor(position_x,1);
  lcd.write(6);
  lcd.write(6);
  lcd.write(2);
  lcd.setCursor(position_x,2);
  lcd.write(7);
  lcd.write(7);
  lcd.write(5); 
}

void digit4(int position_x)
{
  lcd.setCursor(position_x,1);
  lcd.write(3);
  lcd.write(4);
  lcd.write(2);
  lcd.setCursor(position_x+2,2);
  lcd.write(5);
}

void digit5(int position_x)
{
  lcd.setCursor(position_x,1);
  lcd.write((byte)0);
  lcd.write(6);
  lcd.write(6);
  lcd.setCursor(position_x,2);
  lcd.write(7);
  lcd.write(7);
  lcd.write(5);
}

void digit6(int position_x) 
{
  lcd.setCursor(position_x,1);
  lcd.write((byte)0);
  lcd.write(6);
  lcd.write(6);
  lcd.setCursor(position_x,2);
  lcd.write(3);
  lcd.write(7);
  lcd.write(5);
}

void digit7(int position_x)
{
  lcd.setCursor(position_x,1);
  lcd.write(1);
  lcd.write(1);
  lcd.write(2);
  lcd.setCursor(position_x+1,2);
  lcd.write((byte)0);
}

void digit8(int position_x)
{
  lcd.setCursor(position_x,1);
  lcd.write((byte)0);
  lcd.write((byte)6);
  lcd.write(2);
  lcd.setCursor(position_x,2);
  lcd.write(3);
  lcd.write(7);
  lcd.write(5);
}

void digit9(int position_x)
{
  lcd.setCursor(position_x,1);
  lcd.write((byte)0);
  lcd.write((byte)6);
  lcd.write((byte)2);
  lcd.setCursor(position_x+2,2);
  lcd.write((byte)5);
}

int getSubscribers()
{
  WiFiClientSecure client;
  Serial.print("connecting to "); Serial.println(host);
  if (!client.connect(host, 443)) {
    Serial.println("connection failed");
    return -1;
  }
  String cmd = String("GET /youtube/v3/channels?part=statistics&id=") + channelId + "&key=" + apiKey+ " HTTP/1.1\r\n" +
                "Host: " + host + "\r\nUser-Agent: ESP8266/1.1\r\nConnection: close\r\n\r\n";
  client.print(cmd);

  int repeatCounter = 10;
  while (!client.available() && repeatCounter--) {
    delay(500);
  }
  String line,buf="";
  int startJson=0;
  
  while (client.connected() && client.available()) {
    line = client.readStringUntil('\n');
    if(line[0]=='{') startJson=1;
    if(startJson) 
    {
      for(int i=0;i<line.length();i++)
        if(line[i]=='[' || line[i]==']') line[i]=' ';
      buf+=line+"\n";
    }
  }
  client.stop();

  DynamicJsonBuffer jsonBuf;
  JsonObject &root = jsonBuf.parseObject(buf);
  if (!root.success()) {
    Serial.println("parseObject() failed");
    delay(10);
    return -1;
  }
  
  subscribers = root["items"]["statistics"]["subscriberCount"];
  Serial.println(subscribers);
  return subscribers;
}

void createCustomChars()
{
  lcd.createChar(0,LT);
  lcd.createChar(1,UB);
  lcd.createChar(2,RT);
  lcd.createChar(3,LL);
  lcd.createChar(4,LB);
  lcd.createChar(5,LR);
  lcd.createChar(6,UMB);
  lcd.createChar(7,LMB);
}


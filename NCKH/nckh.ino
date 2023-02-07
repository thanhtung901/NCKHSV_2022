#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include  "FirebaseESP8266.h"
#include <WiFiClient.h>
#include <Arduino_JSON.h>
const char* ssid = "CTD.TNUT";
const char* password = "123456789";
#define quat D6
#define den D5
//Your Domain name with URL path or IP address with path
String serverName = "http://192.168.1.107:8000";
#define FIREBASE_HOST "https://nckh-app-default-rtdb.firebaseio.com/" // mã truy cập cơ sở dữ liệu trên firebase
//đường link truy cập đến cơ sở dữ liệu đã tạo trên firebase 

#define FIREBASE_AUTH "JFc2wHsdy15ykBwnfJlXRwx5pmVhMRuBEJDX5m46" // chuỗi bảo mật
// the following variables are unsigned longs because the time, measured in
// milliseconds, will quickly become a bigger number than can be stored in an int.
unsigned long lastTime = 0;
// Timer set to 10 minutes (600000)
//unsigned long timerDelay = 600000;
// Set timer to 5 seconds (5000)
unsigned long timerDelay = 5000;
String dataArr[1];
FirebaseData fbdo;
FirebaseAuth auth;
FirebaseConfig config;
void setup() {
  // put your setup code here, to run once:
   Serial.begin(9600); 

  WiFi.begin(ssid, password);
  Serial.println("Connecting");
  while(WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());
  Serial.println();
  /* Assign the callback function for the long running token generation task */
  Firebase.begin(FIREBASE_HOST,FIREBASE_AUTH); // sử dụng câu lệnh có sẵn trong thư viện để kết nối tới firebase
  Firebase.reconnectWiFi(true);
  Serial.println("connect success");
  pinMode(quat, OUTPUT);
  digitalWrite(quat, LOW);
  pinMode(den, OUTPUT);
  digitalWrite(den, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
    if(WiFi.status()== WL_CONNECTED){
      WiFiClient client;
      HTTPClient http;
      String url_fan = serverName + "/fan/";
      String url_led = serverName + "/lights/";
      String url_tv = serverName + "/tv/";
      String url_dh = serverName + "/dh/";
      String b = httpGETRequest(url_led);
      String a = httpGETRequest(url_fan);
      String re_led = data(b);
      String result_fan = data(a);
      if (result_fan=="bat")
      {
        digitalWrite(quat, HIGH);
        Firebase.setString(fbdo, "quat/quat", "bat");
      }
      else if (result_fan=="tat")
      {
        digitalWrite(quat, LOW);
        Firebase.setString(fbdo, "quat/quat", "tat");
      }
      Serial.println(result_fan);
      
      if (re_led=="bat")
      {
        digitalWrite(den, HIGH);
        Firebase.setString(fbdo, "den/den", "bat");
      }
      else if (re_led=="tat")
      {
        digitalWrite(den, LOW);
        Firebase.setString(fbdo, "den/den", "tat");
      }
      Serial.println(re_led);
      
    }
    delay(1000);
}
String httpGETRequest(String serverName) {
  WiFiClient client;
  HTTPClient http;
  http.begin(client, serverName);
  
  // Send HTTP POST request
  int httpResponseCode = http.GET();
  
  String payload = "{}"; 
  
  if (httpResponseCode>0) {
//    Serial.print("HTTP Response code: ");
//    Serial.println(httpResponseCode);
    payload = http.getString();
  }
  else {
    Serial.print("Error code: ");
    Serial.println(httpResponseCode);
  }
  // Free resources
  http.end();

  return payload;
}
String data(String data)
{
      JSONVar myObject = JSON.parse(data);
      // JSON.typeof(jsonVar) can be used to get the type of the var
      if (JSON.typeof(myObject) == "undefined") {
        Serial.println("Parsing input failed!");
      }
      
//      Serial.print("JSON object = ");
//      Serial.println(myObject);
    
      // myObject.keys() can be used to get an array of all the keys in the object
      JSONVar keys = myObject.keys();
    
      for (int i = 0; i < keys.length(); i++) {
        JSONVar value = myObject[keys[i]];
//        Serial.print(keys[i]);
//        Serial.print(" = ");
//        Serial.println(value); 
        dataArr[i] = value;
      }
//      Serial.print("1 = ");
//      Serial.println(dataArr[0]);
    return dataArr[0];
}

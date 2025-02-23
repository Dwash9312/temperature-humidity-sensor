#include <DHT.h>

// Pin Definitions
#define DHTPIN 2       // Sensor signal wire connected to Digital Pin 2
#define DHTTYPE DHT11  // Change to DHT11 if using a DHT11 sensor

// Initialize DHT sensor
DHT dht(DHTPIN, DHTTYPE);

void setup() {
    Serial.begin(9600);
    Serial.println("Initializing DHT Sensor...");
    dht.begin();
}

void loop() {
    float tempC = dht.readTemperature();  // Read temperature in Celsius
    float tempF = (tempC * 9.0 / 5.0) + 32.0;  // Convert to Fahrenheit
    float humidity = dht.readHumidity();  // Read humidity

    if (isnan(tempC) || isnan(humidity)) {
        Serial.println("⚠️ Error: Could not read temperature or humidity! Check wiring.");
    } else {
        Serial.print("Temperature (F): ");
        Serial.print(tempF);
        Serial.print(" | Humidity (%): ");
        Serial.println(humidity);
    }

    delay(1800000);  // 30 minutes (1800000 ms)
}

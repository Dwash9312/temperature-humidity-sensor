import serial
import sqlite3
import time

# Configure the Serial Port (CHANGE 'COM3' to match your Arduino port)
SERIAL_PORT = 'COM5'  # Windows: 'COM3', Linux/Mac: '/dev/ttyUSB0'
BAUD_RATE = 9600

# SQLite Database Name
DB_NAME = "temperature_humidity_data.db"

def initialize_database():
    """Creates an SQLite table if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS sensor_log (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp TEXT,
                        temperature_f REAL,
                        humidity REAL)''')

    conn.commit()
    conn.close()

def save_to_database(temp_f, humidity):
    """Saves the temperature and humidity reading to SQLite."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("INSERT INTO sensor_log (timestamp, temperature_f, humidity) VALUES (?, ?, ?)",
                   (timestamp, temp_f, humidity))

    conn.commit()
    conn.close()
    print(f"✅ Logged: {timestamp} | Temperature (F): {temp_f} | Humidity (%): {humidity}")

def get_sensor_reading(ser):
    """Reads one temperature & humidity value from Arduino"""
    while True:
        try:
            raw_data = ser.readline().decode('utf-8').strip()  # Read & clean data
            if "Temperature (F):" in raw_data and "Humidity (%):" in raw_data:
                parts = raw_data.split("|")
                temp_f = float(parts[0].split(":")[1].strip())  # Extract temperature
                humidity = float(parts[1].split(":")[1].strip())  # Extract humidity

                return temp_f, humidity  # Return valid values

            else:
                print("⚠️ No valid data received. Retrying...")

        except Exception as e:
            print(f"⚠️ Serial Read Error: {e}")
            break  # Exit if an error occurs

def read_serial():
    """Reads one immediate temperature & humidity value, then waits 30 minutes for the next."""
    while True:
        try:
            print("🔄 Connecting to Arduino...")
            ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=30)
            time.sleep(2)  # Allow time for connection

            # Take an **initial reading immediately**
            print("📌 Taking first reading now...")
            temp_f, humidity = get_sensor_reading(ser)
            if temp_f is not None and humidity is not None:
                save_to_database(temp_f, humidity)

            # Now start the 30-minute loop
            while True:
                print("⏳ Waiting 30 minutes for next reading...")
                time.sleep(1800)  # Wait 30 minutes

                print("📌 Taking next reading...")
                temp_f, humidity = get_sensor_reading(ser)
                if temp_f is not None and humidity is not None:
                    save_to_database(temp_f, humidity)

        except Exception as e:
            print(f"⚠️ Connection Error: {e}")
            print("🔄 Retrying in 10 seconds...")
            time.sleep(10)  # Wait before trying to reconnect

if __name__ == "__main__":
    initialize_database()
    read_serial()

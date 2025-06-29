import time                   # Allows use of time.sleep() for delays
from mqtt import MQTTClient   # For use of MQTT protocol to talk to Adafruit IO
import machine                # Interfaces with hardware components
from machine import Pin       # Define pin
import dht                    # DHT sensor library
import keys                   # Contain all keys used here
import wifiConnection         # Contains functions to connect/disconnect from WiFi 

# BEGIN SETTINGS
SENSOR_INTERVAL = 30000     # time between radings (subject to change)
last_sensor_sent_ticks = 0  # milliseconds

# Hardware initialization
dhtSensor = dht.DHT11(Pin(27))  # DHT11 connected to GPIO pin 27

# Method to read the DHT11 sensor and publish data to Adafruit IO
def sendSensorData():
    global last_sensor_sent_ticks
    global SENSOR_INTERVAL
    
    # Make sure I don't read the sensor too often
    if ((time.ticks_ms() - last_sensor_sent_ticks) < SENSOR_INTERVAL):
        return  # To early to read sensor, skip this time
    
    try:
        # Make sure the sensor is ready
        dhtSensor.measure()
        temperature = dhtSensor.temperature()  # Temperature in Celsius
        humidity = dhtSensor.humidity()        # Humidity percentage
        
        print("Temperature: {}°C, Humidity: {}%".format(temperature, humidity))
        
        # Publish temperature to Adafruit IO
        print("Publishing temperature: {} to Adafruit IO...".format(temperature), end=' ')
        try:
            client.publish(topic=keys.AIO_TEMPERATURE_FEED, msg=str(temperature))
            print("SUCCESS")
        except Exception as e:
            print("FAILED:", e)
        
        # Publish humidity to Adafruit IO
        print("Publishing humidity: {} to Adafruit IO...".format(humidity), end=' ')
        try:
            client.publish(topic=keys.AIO_HUMIDITY_FEED, msg=str(humidity))
            print("SUCCESS")
        except Exception as e:
            print("FAILED:", e)
            
    except OSError as e:
        print("Failed to read DHT11 sensor:", e)
        print("Check sensor wiring and connections")
    except Exception as e:
        print("Unexpected sensor error:", e)
    finally:
        last_sensor_sent_ticks = time.ticks_ms()

# Connect to WiFi
try:
    print("Connecting to WiFi...")
    ip = wifiConnection.connect()
    print("Connected! IP:", ip)
except KeyboardInterrupt:
    print("Keyboard interrupt")
except Exception as e:
    print("WiFi connection failed:", e)

# Connect to Adafruit IO using MQTT
print("Connecting to Adafruit IO...")
client = MQTTClient(keys.AIO_CLIENT_ID, keys.AIO_SERVER, keys.AIO_PORT, keys.AIO_USER, keys.AIO_KEY)

try:
    client.connect()
    print("Connected to Adafruit IO successfully!")
except Exception as e:
    print("Failed to connect to Adafruit IO:", e)

# Main script loop
# The loop will run indefinitely, reading the sensor and sending data at specified intervals
print("Starting sensor monitoring...")
print("Reading sensor every {} seconds".format(SENSOR_INTERVAL // 1000))

try:
    while True:  # Run forever
        sendSensorData()  # Check if it's time to read sensor and send data
        time.sleep(1)       # Small delay to protect the CPU from being overloaded
        
except KeyboardInterrupt:
    print("\nProgram interrupted by user")
except Exception as e:
    print("Unexpected error in main loop:", e)
finally:
    # Clean up connections
    try:
        client.disconnect()
        print("Disconnected from Adafruit IO")
    except:
        pass
    
    try:
        wifiConnection.disconnect()
        print("Disconnected from WiFi")
    except:
        pass
    
    print("Program ended")
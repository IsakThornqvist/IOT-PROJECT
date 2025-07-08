import time
from mqtt import MQTTClient
import machine
from machine import Pin
import dht
import keys
import wifiConnection

# sensor settings
sensorInterval = 30000
lastSentTime = 0

dhtSensor = dht.DHT11(Pin(27))

# function to send sensor data to Adafruit IO
def sendSensorData():
    global lastSentTime
    global sensorInterval
    
    # time checker
    if ((time.ticks_ms() - lastSentTime) < sensorInterval):
        return
    
    try:
        dhtSensor.measure()
        temperature = dhtSensor.temperature()
        humidity = dhtSensor.humidity()
                
        print("Publishing temperature: {} to Adafruit IO.".format(temperature), end=' ')
        try:
            client.publish(topic=keys.AIO_TEMPERATURE_FEED, msg=str(temperature))
            print("SUCCESS")
        except Exception as e:
            print("FAILED:", e)
        
        print("Publishing humidity: {} to Adafruit IO.".format(humidity), end=' ')
        try:
            client.publish(topic=keys.AIO_HUMIDITY_FEED, msg=str(humidity))
            print("SUCCESS")
        except Exception as e:
            print("FAILED:", e)
            
    except OSError as e:
        print("DHT11 error", e)
    except Exception as e:
        print("Sensor error:", e)
    finally:
        lastSentTime = time.ticks_ms()

# connect to WiFi
try:
    ip = wifiConnection.connect()
    print("Connected! IP:", ip)
except Exception as e:
    print("WiFi connection failed:", e)

# connect to Adafruit IO using MQTT
print("Connecting to Adafruit IO...")
client = MQTTClient(keys.AIO_CLIENT_ID, keys.AIO_SERVER, keys.AIO_PORT, keys.AIO_USER, keys.AIO_KEY)

try:
    client.connect()
    print("Connected to Adafruit IO!")
except Exception as e:
    print("Failed to connect to Adafruit IO:", e)

print("Reading sensor every {} seconds".format(sensorInterval // 1000))

try:
    while True:
        sendSensorData()
        time.sleep(1)
        
except KeyboardInterrupt:
    print("\nProgram interrupted by user")
except Exception as e:
    print("Error in main loop:", e)
finally:
    # clean up and disconnect
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
#  Temperature & Humidity Sensor with Adafruit IO

**By it222hp**

## Project Overview

This project demonstrates how to build an IoT temperature and humidity sensor using a DHT11 sensor and a Raspberry Pi Pico W. The device reads environmental data and transmits it to Adafruit IO using the MQTT protocol.

- **Estimated Time**: 12-18h
- **Skill Level**: Beginner

---

## Objective

I chose to build this sensor because indoor climate monitoring is valuable for comfort. With real-time temperature and humidity data accessible from anywhere, I can gain new insights into my environment and monitor how the temprature and humidity changes.

- **Why this project?** Simple but practical use of IoT for real-world sensing  
- **Purpose**: Collect and send environmental data to the Adafruit
- **Insights expected**: Understand more about IoT and the DHT11 sensor

---

## Materials

| Component            | Purpose                          | Source         |
|---------------------|----------------------------------|----------------|
| Raspberry Pi Pico W | Microcontroller with WiFi        | [Elektrokit](https://www.electrokit.com/lnu-starter)  |
| DHT11 Sensor         | Measures temperature & humidity  | [Elektrokit](https://www.electrokit.com/lnu-starter)  |
| Wires         | For connections                  | [Elektrokit](https://www.electrokit.com/lnu-starter)  |
| Breadboard           | Prototyping connections          | [Elektrokit](https://www.electrokit.com/lnu-starter)  |
| Micro USB Cable      | Power and programming            | [Elektrokit](https://www.electrokit.com/lnu-starter)  |

>  *The LNU starter kit costs 349 SEK and includes all needed components for this project*

---
> ![image](https://github.com/user-attachments/assets/fbb64cc1-1975-4b12-99f3-9d51146eba9f)

> 📸 *The LNU starter kit*


# Getting Started with Raspberry Pi Pico W and MicroPython

## Prerequisites

Before you begin, ensure you have the following:

-  All required materials listed above (e.g., Raspberry Pi Pico W, Micro USB cable, etc.)

---

## Installing MicroPython Firmware

1. **Download the MicroPython firmware**  
   - Head over to the official Raspberry Pi Pico MicroPython page and grab the latest UF2 firmware for the Pico W.

2. **Connect the Pico W to your computer**  
   - Hold down the **BOOTSEL** button on the Pico W.  
   - While holding it, connect the board to your computer using a USB cable.  
   - Release the BOOTSEL button after connecting.

3. **Add MicroPython to Your Pico W**  
   - Your Pico W should appear as a **storage device** on your computer.  
   - Drag and drop or copy the downloaded **UF2 file** onto this device.  
   - The Pico W will automatically restart itself and should now be shown as a USB serial device.

---

## Installing VSCode and Pymakr Plugin

1. **Install Visual Studio Code**  
   - Download and install it from the [official VSCode website](https://code.visualstudio.com/).

2. **Install the Pymakr Plugin**  
   - Open VSCode and go to the **Extensions** view (click the Extensions icon in the sidebar on the left side of the VSCode ui).  
   - Search for **Pymakr** by **Pycom** and click **Install**.

3. **Configure Pymakr Plugin**  
   - Click the **Pymakr icon** in the VSCode status bar.  
   - With your Pico W connected, you should see a list of devices.  
   - Hover over your device and click **Connect Device**.  

---

## Software Setup

1. **Install Node.js**  
   - Download and install Node.js from the [official website](https://nodejs.org/).
     
---

## Get Your Code onto the Pico W

1. **Create your MicroPython project**  
   - In VSCode you now need to create a new folder for your project.  
   - Inside the folder, create a Python file called main.py and add your MicroPython code there.

2. **Connect the computer to the Pico W**  
   - Make sure your Pico W is connected via USB.  
   - Click the **Pymakr icon** in the left sidebar and select the connect button **Connect**.

3. **Upload the code**  
   - Once connected, click **Sync Project to Device** from the Pymakr sidebar.  
   - Your code will be uploaded and executed on the Pico W.  
   - Optionally, enable **Development Mode** to auto-upload and restart the device on file changes.


---

## Wiring / Circuit Diagram

- **DHT11 to Pico W connections**:

![image](https://github.com/user-attachments/assets/3e130d46-c391-4f37-b86e-a9b10d97a70f)

> 📷 *This is my setup for this project*


![image](https://github.com/user-attachments/assets/ae0f405f-653d-4423-8792-f72e2822d633)

> 📷 *Circuit Diagram*

---

## Platform Choice

- **Platform**: Adafruit IO
- **Why Adafruit IO?** Free for basic use, easy integration with MQTT, great dashboards  
- **Plan**: Free plan

---

## The Code (Core Logic)

The code is devided into several diffrent files for clarity, some of the most important parts are:

1. Wi-Fi Setup (wifiConnection.py)
```python
def connect():
    wlan = network.WLAN(network.STA_IF)         # Put modem on Station mode
    if not wlan.isconnected():                  # Check if already connected
        print('connecting to network...')
        wlan.active(True)                       # Activate network interface
        # set power mode to get WiFi power-saving off (if needed)
        wlan.config(pm = 0xa11140)
        wlan.connect(keys.WIFI_SSID, keys.WIFI_PASS)  # Your WiFi Credential
        print('Waiting for connection...', end='')
        # Check if it is connected otherwise wait
        while not wlan.isconnected() and wlan.status() >= 0:
            print('.', end='')
            sleep(1)
    # Print the IP assigned by router
    ip = wlan.ifconfig()[0]
    print('\nConnected on {}'.format(ip))
    return ip


```
>  *This function manages the Wi-Fi connection. It activates the network interface, connects using saved credentials, and waits until the connection is established. Disabling power saving helps maintain a stable link. Finally, it returns the assigned IP address. This is important for being able to data transmission to Adafruit. IO.*

 2. Sensor Initialization & Data Handling (main.py)
```python
dhtSensor = dht.DHT11(Pin(27))

# function to send sensor data to Adafruit IO
def sendSensorData():
    global last_sensor_sent_ticks
    global SENSOR_INTERVAL
    
    # time checker
    if ((time.ticks_ms() - last_sensor_sent_ticks) < SENSOR_INTERVAL):
        return
    
    try:
        dhtSensor.measure()
        temperature = dhtSensor.temperature()
        humidity = dhtSensor.humidity()
                
        print("Publishing temperature: {} to Adafruit IO...".format(temperature), end=' ')
        try:
            client.publish(topic=keys.AIO_TEMPERATURE_FEED, msg=str(temperature))
            print("SUCCESS")
        except Exception as e:
            print("FAILED:", e)
        
        print("Publishing humidity: {} to Adafruit IO...".format(humidity), end=' ')
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
        last_sensor_sent_ticks = time.ticks_ms()

```
>  *This function is responsible for collecting temperature and humidity data from the DHT11 sensor and publishing it to Adafruit IO via MQTT.*

 3. MQTT Connection Setup (main.py)
```python
# connect to Adafruit IO using MQTT
print("Connecting to Adafruit IO...")
client = MQTTClient(keys.AIO_CLIENT_ID, keys.AIO_SERVER, keys.AIO_PORT, keys.AIO_USER, keys.AIO_KEY)

try:
    client.connect()
    print("Connected to Adafruit IO!")
except Exception as e:
    print("Failed to connect to Adafruit IO:", e)

```
>  *This snippet sets up the MQTT client and that then allows the device to communicate with Adafruit. If this connection was not there, sensor data would not be able to be sent to the dashboard.*

## Transmitting the data / Connectivity

The DHT11 sensor data (temperature and humidity) is transmitted to the internet using Wi-Fi and sent to Adafruit IO using the MQTT protocol. The main steps involved are:

- Wi-Fi Connection:
The Raspberry Pi Pico W connects to a local Wi-Fi network using credentials stored in keys.py. This is handled in wifiConnection.py.

- Reading Sensor Data:
Every 30 seconds, the Pico W reads temperature and humidity data from the DHT11 sensor connected to GPIO 27.

- Preparing the Data:
The sensor values are converted to strings and published using the MQTT client.

- Sending the Data:
The data is sent over the Wi-Fi network using the MQTT protocol to Adafruit IO, where it is displayed on a dashboard.

## Communication flow
DHT11 sensor -> Read data on Pico W -> Convert to String -> MQTT publish() -> Send over Wi-Fi -> MQTT protocoll to Adafruit.io -> Data visible on dashboard

## Package Format
The transport protocal used was MQTT (Message Queuing Telemetry Transport) which is a lightweight messaging protocol used to publish the sensor data to Adafruit IO.

   The MQTT messages contains:
   - Topic (e.g., username/feeds/temperature or username/feeds/humidity)
   - Payload: String of the sensor value (e.g., 25 or 56)


## Presenting the data

![image](https://github.com/user-attachments/assets/1ff5c080-709e-4589-891e-b71341ef9db4)

> 📷 *The data visualized on the Adafruit dashboard*


## Finalizing the design

The Temperature and Humidity project turned out as expected. Readings from the DHT11 sensor are successfully transmitted every 30 seconds and displayed in real-time on the Adafruit IO dashboard.

## Results

   - Reliable sensor readings at 30 second intervals.
   - Data transmission over WI-FI using the Raspberry Pi
   - Live updates that you can view in the Adafruit dashboard  

## Reflection

When I started this project, I had no idea what to expect. All of the components I ordered from Elektrokit were completely new to me, and I had never interacted with them before. The learning curve was steep, especially during the first few weeks of the course.

Although I had prior programming experience in Java and JavaScript, Python was completely new to me. Fortunately, the course had a well-structured format. Each week had a clear focus, and the roadmap provided a helpful overview of what was coming up next. This structure made the process more manageable and allowed me to build up my knowledge step by step both in programming and hardware.

For the project itself, I decided to go with a relatively simple idea—one that still gave me room to learn and that could easily be expanded in the future if desired.

Possible improvements
   - Use a more advanced sensor, or include additional sensors to measure different environmental variables like light.
   - The Pico W itself is currently very exposed, if used outdoors it could get damaged so some sort of protection around the build could be of use.
   - The dashboard itself could be more advanced. For example: show average temperature over a day, add additional visual components (e.g., gauges, indicators) or even allowing to switch between diffrent timeframes for more precise data views

## Final Product

![image](https://github.com/user-attachments/assets/7e71694e-7582-42a0-919b-10029ae7349b)

![image](https://github.com/user-attachments/assets/565587c6-0610-41cf-9977-9236d23e0ea0)

![image](https://github.com/user-attachments/assets/f242c6c8-a05f-468c-a632-b7da0f2bc3d5)






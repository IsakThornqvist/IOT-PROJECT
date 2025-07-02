#  Temperature & Humidity Sensor with Adafruit IO

**By Isak Thörnqvist (it222hp)**

## Project Overview

This project demonstrates how to build an IoT temperature and humidity sensor using a DHT11 sensor and a Raspberry Pi Pico W. The device reads environmental data and transmits it to Adafruit IO using the MQTT protocol.

- **Estimated Time**: 20h
- **Skill Level**: Beginner to Intermediate

---

## Objective

I chose to build this sensor because indoor climate monitoring is valuable for comfort. With real-time temperature and humidity data accessible from anywhere, I can gain new insights into my environment and monitor how the temprature and humidity changes.

- **Why this project?** Simple but practical use of IoT for real-world sensing  
- **Purpose**: Collect and send environmental data to the Adafruit
- **Insights expected**: Understand more about IoT and the DHT11 sensor

---

## Materials

| Component            | Purpose                          | Source         | Cost     |
|---------------------|----------------------------------|----------------|----------|
| Raspberry Pi Pico W | Microcontroller with WiFi        | [Elektrokit](https://www.electrokit.com/lnu-starter)  | ???    |
| DHT11 Sensor         | Measures temperature & humidity  | [Elektrokit](https://www.electrokit.com/lnu-starter)  | ???    |
| Wires         | For connections                  | [Elektrokit](https://www.electrokit.com/lnu-starter)  | ???    |
| Breadboard           | Prototyping connections          | [Elektrokit](https://www.electrokit.com/lnu-starter)  | ???    |
| Micro USB Cable      | Power and programming            | [Elektrokit](https://www.electrokit.com/lnu-starter)  | ???    |

---
> ![image](https://github.com/user-attachments/assets/fbb64cc1-1975-4b12-99f3-9d51146eba9f)

> 📸 *The LNU starter kit*


## Computer Setup

- **IDE Used**: Visual Studio Code  
- **Firmware**: MicroPython v1.25.0  
- **Steps**:

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

> 🆚 *Possible Alternatives*: ThingsBoard, Node-RED

---

## The Code (Core Logic)

```python
import time
....
...
...

```

## Transmitting the data / Connectivity

## Presenting the data

![image](https://github.com/user-attachments/assets/1ff5c080-709e-4589-891e-b71341ef9db4)

> 📷 *The data visualized on the Adafruit dashboard*


## Finalizing the design




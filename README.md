# 🌡️ Temperature & Humidity Sensor with Adafruit IO

**By Isak Thörnqvist (it222hp)**

## 📝 Project Overview

This project demonstrates how to build an IoT temperature and humidity sensor using a DHT11 sensor and a Raspberry Pi Pico W. The device reads environmental data and transmits it to Adafruit IO using the MQTT protocol.

- **Estimated Time**: ??? 
- **Skill Level**: Beginner to Intermediate

---

## 🎯 Objective

I chose to build this sensor because indoor climate monitoring is valuable for comfort. With real-time temperature and humidity data accessible from anywhere, I can gain new insights into my environment and monitor how the temprature and humidity changes.

- **Why this project?** Simple but practical use of IoT for real-world sensing  
- **Purpose**: Collect and send environmental data to the Adafruit
- **Insights expected**: Understand more about IoT and the DHT11 sensor

---

## 🧰 Materials

| Component            | Purpose                          | Source         | Cost     |
|---------------------|----------------------------------|----------------|----------|
| Raspberry Pi Pico W | Microcontroller with WiFi        | ???  | ???    |
| DHT11 Sensor         | Measures temperature & humidity  | ???  | ???    |
| Wires         | For connections                  | ???  | ???       |
| Breadboard           | Prototyping connections          | ???  | ???       |
| Micro USB Cable      | Power and programming            | ???  | ???    |

> 📸 *Photos*

---

## 💻 Computer Setup

- **IDE Used**: Visual Studio Code  
- **Firmware**: MicroPython v1.25.0  
- **Steps**:

---

## 🔌 Wiring / Circuit Diagram

- **DHT11 to Pico W connections**:


> 📷 *Picture here*

---

## ☁️ Platform Choice

- **Platform**: Adafruit IO
- **Why Adafruit IO?** Free for basic use, easy integration with MQTT, great dashboards  
- **Plan**: Free plan

> 🆚 *Possible Alternatives*: ThingsBoard, Node-RED

---

## 🧠 The Code (Core Logic)

```python
import time
....
...
...

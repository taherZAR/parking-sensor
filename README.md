# 📏 Distance Detector with Ultrasonic Sensor (ESP32/ESP8266)

A simple MicroPython project that uses an HC-SR04 ultrasonic sensor to measure distance. When an object is detected closer than 100 cm, the built-in LED is turned on.

---

## 🧰 Components Used

- 🧠 ESP32 or ESP8266 microcontroller
- 📏 HC-SR04 ultrasonic distance sensor
- 💡 Onboard LED (usually on pin 2)
- ⚡ MicroPython firmware
- 🖥️ USB cable and serial terminal (e.g., Thonny or uPyCraft)

---

## 🔌 Pin Connections

| HC-SR04 Pin | ESP32/ESP8266 Pin |
|-------------|-------------------|
| VCC         | 3.3V or 5V        |
| GND         | GND               |
| TRIG        | D3 or GPIO3       |
| ECHO        | D2 or GPIO2       |

> ⚠️ Make sure to use valid GPIO pins for your board.

---

## 📄 How It Works

- Sends a 10μs pulse from the TRIG pin
- Measures the time for the echo to return
- Calculates the distance in centimeters
- If distance < 100 cm → turns on the LED
- Else → LED is off

---

## 🧠 Code Overview

```python
from machine import Pin, time_pulse_us
from time import sleep

TRIG = Pin(3, Pin.OUT)
ECHO = Pin(2, Pin.IN)
LED = Pin(2, Pin.OUT)

def read_distance_cm():
    TRIG.value(0)
    sleep(0.000002)
    TRIG.value(1)
    sleep(0.00001)
    TRIG.value(0)
    try:
        duration = time_pulse_us(ECHO, 1, 30000)
        return (duration * 0.0343) / 2
    except OSError:
        return -1

while True:
    distance = read_distance_cm()
    if 0 < distance < 100:
        LED.on()
    else:
        LED.off()
    print("Measured distance:", distance, "cm")
    sleep(0.1)
🚀 Getting Started
Flash MicroPython to your board.

Upload the code using Thonny, uPyCraft, or ampy.

Open the serial monitor.

Move an object closer or farther to see the LED behavior and distance readout.

📦 License
This project is open-source and free to use under the MIT License.

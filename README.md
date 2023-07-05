# Stroller IoT Project with Raspberry Pi Pico W
**Author:** Nasit Vurgun (nv222ek), July 2023

![](https://hackmd.io/_uploads/H1rHToZt2.png)

**Overview**: Stroller IoT is a smart stroller project using the Raspberry Pi Pico W that includes a temperature and humidity sensor, indicator lights, and a social networking component. The purpose is to allow parents with strollers to monitor the environment, so they can take actions to ensure the comfort of their child. Another purpose of the project is to enable parents with strollers to socialize when they are in close proximity or approaching each other (within 10 meters).

The project hardware includes the Raspberry Pi Pico W, a DHT11 sensor, LED indicators, a push button, and a 38 kHz IR transmitter/sensor pair. The software includes an Adafruit IoT dashboard.

**Time**: 10-12 hours to complete, depending on skill level.

## Objective
As a parent, I am constantly monitoring the well-being of my child, especially on hot and humid summer days. Sometimes, the weather changes quickly, and rain approaches during a leisurely walk through the neighborhood. Other times, my wife wishes to meet other parents so that she can make friends and so that our children can play together. This is the reason I came up with this project. Parents like us might want to use a smart stroller with sensors and indicators to keep their child safe and comfortable. With the temperature and humidity sensor, parents can make sure that their child doesn't get too hot or too cold. The indicator lights help parents to quickly check if everything is okay in the stroller and to take action if needed. Many parents have complained of social isolation after having children. By enabling the social feature, parents can easily meet other parents with strollers, without sharing their sensitive personal data with third-party mobile apps.

## Materials

| Image | Component | Description | Cost |
| -------- | -------- | -------- | -------- |
|<img src="https://hackmd.io/_uploads/BJdF4p-t2.jpg" width="50%" height="50%">| Raspberry Pi Pico W (or WH)| Microcontroller board with Wi-Fi for embedded projects. | Elecrokit 98kr (109kr) |
|<img src="https://hackmd.io/_uploads/Syvv4a-F3.jpg" width="50%" height="50%">| Breadboard | Solderless prototyping board for circuit design. | Electrokit 69kr|
|<img src="https://hackmd.io/_uploads/SJezV6ZFn.jpg" width="50%" height="50%">| DHT11 Temperature and Humidity Sensor| Sensor module for measuring temperature and humidity. | Electrokit 49kr|
|<img src="https://hackmd.io/_uploads/rkstmT-K2.jpg" width="50%" height="50%">| 38 kHz IR Transmitter| Infrared transmitter for remote control applications. | Electrokit 26kr|
|<img src="https://hackmd.io/_uploads/Hy8yNTWtn.jpg" width="50%" height="50%">| 38 kHz IR Receiver| Infrared receiver for remote control applications. | Electrokit 32kr|
|<img src="https://hackmd.io/_uploads/HJdWTaZt3.jpg" width="50%" height="50%">| LED 5mm Green| Green LED for visual indicators. | Electrokit 5kr|
|<img src="https://hackmd.io/_uploads/rJA-TaWKn.jpg" width="50%" height="50%">| LED 5mm Yellow| Yellow LED for visual indicators. | Electrokit 5kr|
|<img src="https://hackmd.io/_uploads/rk7Gp6Wt3.jpg" width="50%" height="50%">| LED 5mm Red| Red LED for visual indicators. | Electrokit 5kr|
|<img src="https://hackmd.io/_uploads/HyhryAbYh.jpg" width="50%" height="50%">| LED module color changing| RGB LED module capable of color changing. | Electrokit 15kr|
|<img src="https://hackmd.io/_uploads/Byp5ICZt3.jpg" width="50%" height="50%">| Tilt switch| Tilt switch with rolling ball. | Electrokit 12kr|
|<img src="https://hackmd.io/_uploads/rySTSCZt2.jpg" width="50%" height="50%">| 3x330, 1x10k Resistors | Current-limiting 330 Ohm resistor for each of LEDs. 10kOhm pull-up resistor for tilt switch. | Electrokit 99kr|
|<img src="https://hackmd.io/_uploads/H1baAa-Kh.jpg" width="50%" height="50%">| Momentary Push Button| Momentary switch for user input. | Electrokit 19kr|
|<img src="https://hackmd.io/_uploads/BJWo6aZKh.jpg" width="50%" height="50%">| Jumper wires, male-male, 30cm| Male-to-male jumper wires for easy circuit connections. | Electrokit 29kr|
|<img src="https://hackmd.io/_uploads/rkbIAp-t3.jpg" width="50%" height="50%">| USB-A micro Cable| USB-A to micro USB cable for power and data connections. | Electrokit 39kr|
|<img src="https://hackmd.io/_uploads/HyYP2hWt3.jpg" width="50%" height="50%">| Hama PowerBank - 20000 mAh| Portable power bank with 20000 mAh capacity. | Bauhaus 379kr|


## Computer setup
Follow these steps to install Thonny and flash firmware on the Raspberry Pi Pico W.

1. Download and install the Raspberry Pi Pico W [MicroPython UF2 firmware](https://micropython.org/download/rp2-pico-w/rp2-pico-w-latest.uf2):
Connect your Raspberry Pi Pico W to your computer via USB, holding the **BOOTSEL button** down. Release BOOTSEL button. Drag and drop the MicroPython UF2file onto the RPI-RP2 volume Mass Storage Device. The Pico should reboot. That's it, firmware has been flashed.

2. Choose your interpreter (Thonny or VS Code):
**Thonny IDE**: Download and install [Thonny](https://thonny.org/). In Thonny, go to **File** -> **Open...** and navigate to the extracted firmware folder. Select ***MicroPython (Raspberry Pi Pico) - COM5*** as your interpreter, in the bottom right hand corner of Thonny window. Create a new folder, called **Stroller_IoT**. Save your .py files to Raspberry Pi Pico to update the device. You can install packages from **Run** -> **Manage Packages...** which will save them to the lib folder.
-or-
**VS Code**: Download and install [Visual Studio Code](https://code.visualstudio.com/Download). Download and install [Node.js](https://nodejs.org/en). Install Pymakr using the extensions tab in VS Code ([see here](https://docs.pycom.io/gettingstarted/software/vscode/)). PyMakr will create a new tab (*PP*) in the left hand menu of VS Code. Create a new project, call it **Strolller_IoT**. You should see **USB Serial Device (COM5)** in the Devices menu - hover over this, and click Connect device. Hover over **Stroller_IoT**, and click development mode (*</>*) to enable hot flashing whenever you save new code in the interpreter.

That's it! You have installed Thonny / VS Code and flashed the firmware on Raspberry Pi Pico W.


## Putting everything together
A quick walkthrough what the purpose of each electronic components for this project and how they interact with each other:
* DHT11 measures temperature (degC) and relative humidity (%). Published to Adafruit.
* LED indicators change color depending on temperature (solid green if ideal, flashes red if its outside optimal range), and humidity preferences (yellow lights up if it's very humid).
* Tilt switch turns on pico PCB on-board LED. This functions as vibration sensor.
* Button press enables the IR transmitter/receiver. Press it while approaching another stroller.
* If 30 consecutive IR signals are received within short duration, AdaFruit is notified. Discord message is sent through webhook. RGB LED lights up for 10 seconds (default setting).

**Circuit Diagram**:
![](https://hackmd.io/_uploads/ry2C4yzKn.png)
**Disconnect USB from powerbank or computer end before you connect any pins.** Verify sensor polarity from sensor/LED datasheets. Refer to the [Pinout Diagram]() for the Raspberry Pi Pico W.

You need to use a 10 kOhm resistor to pull-up the voltage for the tilt switch sensor. You need 330 Ohm resistors for each of the LEDs to limit the current. Power device from laptop or power bank.

## Platform
I chose [Adafruit IO](https://io.adafruit.com/), a cloud-based platform with webhooks for my IoT project. It is well-suited for small-scale projects and offers beginner-friendly features, free usage, and simple management. The free version allows for 5 feeds and 30 messages per minute, with the option to upgrade for a fee. Adafruit requires minimal coding on the back-end, which made it simple to make a front-end client for my project. I also implemented webhooks to send messages to Discord, which is a really neat feature that is available on Adafruit.

## The Code
Start by downloading `mqtt.py` from [here](https://github.com/iot-lnu/applied-iot/blob/master/Pycom%20Micropython%20(esp32)/network-examples/mqtt_ubidots/mqtt.py). Upload it to the Raspberry Pi Pico W.

Download `main.py` found on my GitHub [here](https://github.com/vurg/stroller-iot/blob/main/main.py), and upload it to the Pico.

Create a `secrets.py` with your Wi-Fi details, and Adafruit key. Upload it to the Pico device:

```
secrets = {
   'ssid' : 'YOUR_WIFI_NETWORK_SSID_NAME',
   'password' : 'YOUR_WIFI_NETWORK_PASSWORD',
   'ada_key' : 'YOUR_ADAFRUIT_IO_KEY',
   }
```


**This section is under construction. Detailed explanations to follow.**


# Transmitting the data / connectivity
Temperature and humidity measurements are published on the [Adafruit dashboard](https://io.adafruit.com/stroller/dashboards/mydashboard) every minute. Adafruit.io has built in actions using webhooks that send discord messages. Firstly, we are notified on discord when we encounter another friendly stroller. Secondly, we are alerted when temperature and huidity are much higher than the desired range. My project uses Wi-Fi, typically through a cellphone that has hotspot enabled. Once Wi-Fi connection is established, messages are sent from the Pico to the Adafruit IO server wtih its MQTT cloud broker. We also subscribe to messages from the MQTT broker for whether the RGB LED should turn on when we turn on the IR transmitter and approach another stroller. Some users may not want this (unwanted attention).

**Note:** The Raspberry Pi Pico W Wi-Fi component is unable to connect to 5G networks!!

# Presenting the data

![](https://hackmd.io/_uploads/BkoBMHfth.png)

The data is published and saved to Adafruit every minute when the device is powered on. Each feed in Adafruit stores the data for 30 days. Webhooks warnings are sent to Discord when temperature is above 26 degC, and humidity is above 70%. The RGB LED feature can also be turned ON or OFF through the Adafruit dashboard. There is also a running text stream that keeps a note of when we bump into someone.


The dashboard is built using feeds and actions, as shown below.
![](https://hackmd.io/_uploads/rkJDGrMY2.png)
![](https://hackmd.io/_uploads/HJSvGBzY2.png)

As an alternative, I tried HiveMQ (encrypted cloud broker), and was able to have an SSL/TLS encrypted connection. If I had more time, I would have built my own back-end with this, and a mobile app with [LoRaWAN Geolocation](https://backend.orbit.dtu.dk/ws/portalfiles/portal/130478296/paper_final_2.pdf). I will also try out the TIG stack in the coming days.

# Finalizing the design
| Prototype with Breadboard + Powerbank| IoT Dashboard |
| -------- | -------- | 
|<img src="https://hackmd.io/_uploads/ryK3T-Mt3.jpg" width="60%" height="60%">|<img src="https://hackmd.io/_uploads/BkoBMHfth.png" width="150%" height="150%">|

**Discord**
![](https://hackmd.io/_uploads/B1Q6WHMF3.png)

**Hackmd link:** https://hackmd.io/@rIFCcdNpR2WfEEjApaiQyw/B1Un8bGFn

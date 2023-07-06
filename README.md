# Stroller IoT Project with Raspberry Pi Pico W
**Author:** Nasit Vurgun (nv222ek)

![](https://hackmd.io/_uploads/H1rHToZt2.png)

**Overview**: Stroller IoT is a smart stroller project using the Raspberry Pi Pico W that includes a temperature and humidity sensor, vibration sensor, indicator lights, and a social networking component. The purpose is to allow parents with strollers to monitor the environment, so they can take actions to ensure the comfort of their child. Another purpose of the project is to enable parents with strollers to socialize when they are in close proximity or approaching each other (within 10 meters).

The project hardware includes the Raspberry Pi Pico W, a DHT11 sensor, LED indicators, a push button, a tilt sensor, and a 38 kHz IR transmitter/sensor pair. The software includes an Adafruit IoT dashboard.

**Time**: 10-12 hours to complete, depending on skill level.

![](https://hackmd.io/_uploads/rykT99GKh.jpg)


# Objective
As a parent, I am constantly monitoring the well-being of my child, especially on hot and humid summer days. Sometimes, the weather changes quickly, and rain approaches during a leisurely walk through the neighborhood. Other times, my wife wishes to meet other parents so that she can make friends and so that our children can play together. This is the reason I came up with this project. Parents like us might want to use a smart stroller with sensors and indicators to keep their child safe and comfortable. With the temperature and humidity sensor, parents can make sure that their child doesn't get too hot or too cold. The indicator lights help parents to quickly check if everything is okay in the stroller and to take action if needed. Many parents have complained of social isolation after having children. By enabling the social feature, parents can easily meet other parents with strollers, without sharing their sensitive personal data with third-party mobile apps.

# Materials

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


# Computer setup
Follow these steps to install Thonny and flash firmware on the Raspberry Pi Pico W.

1. Download and install the Raspberry Pi Pico W [MicroPython UF2 firmware](https://micropython.org/download/rp2-pico-w/rp2-pico-w-latest.uf2):
Connect your Raspberry Pi Pico W to your computer via USB, holding the **BOOTSEL button** down. Release BOOTSEL button. Drag and drop the MicroPython UF2file onto the RPI-RP2 volume Mass Storage Device. The Pico should reboot. That's it, firmware has been flashed.
![](https://hackmd.io/_uploads/S1vd2HMFn.png)
2. Choose your interpreter (Thonny or VS Code):
**Thonny IDE**: Download and install [Thonny](https://thonny.org/). In Thonny, go to **File** -> **Open...** and navigate to the extracted firmware folder. Select ***MicroPython (Raspberry Pi Pico) - COM5*** as your interpreter, in the bottom right hand corner of Thonny window. Create a new folder, called **Stroller_IoT**. Save your .py files to Raspberry Pi Pico to update the device. You can install packages from **Run** -> **Manage Packages...** which will save them to the lib folder.
-or-
**VS Code**: Download and install [Visual Studio Code](https://code.visualstudio.com/Download). Download and install [Node.js](https://nodejs.org/en). Install Pymakr using the extensions tab in VS Code ([see here](https://docs.pycom.io/gettingstarted/software/vscode/)). PyMakr will create a new tab (*PP*) in the left hand menu of VS Code. Create a new project, call it **Strolller_IoT**. You should see **USB Serial Device (COM5)** in the Devices menu - hover over this, and click Connect device. Hover over **Stroller_IoT**, and click development mode (*</>*) to enable hot flashing whenever you save new code in the interpreter.

That's it! You have installed Thonny / VS Code and flashed the firmware on Raspberry Pi Pico W.


# Putting everything together
A quick walkthrough what the purpose of each electronic components for this project and how they interact with each other:
* DHT11 measures temperature (degC) and relative humidity (%). Published to Adafruit.
* LED indicators change color depending on temperature (solid green if ideal, flashes red if its outside optimal range), and humidity preferences (yellow lights up if it's very humid).
* Tilt switch turns on pico on-board LED. It is quite sensitive, so we use it as vibration sensor.
* Button press enables the IR transmitter/receiver. Press it while approaching another stroller.
* If 30 consecutive IR signals are received within short duration, AdaFruit is notified. Discord message is sent through webhook. RGB LED lights up for 10 seconds (default setting).

**Circuit Diagram**:
![](https://hackmd.io/_uploads/rkAf3SXYh.png)

**Disconnect USB from powerbank or computer end before you connect any pins.** Verify sensor polarity from sensor/LED datasheets. Refer to the [Pinout Diagram]() for the Raspberry Pi Pico W. Always follow the manufacturer data sheets when connecting sensors.

You need to use a 10 kOhm resistor to pull-up the voltage for the tilt switch sensor. You need 330 Ohm resistors for each of the LEDs to limit the current. Power device from laptop or power bank.

:warning: **Warning:** Cabling will be a mess (spagetti) on the breadboard -  it is best to use short wires!!

# Platform
I chose [Adafruit IO](https://io.adafruit.com/), a cloud-based platform with webhooks for my IoT project. It is well-suited for small-scale projects and offers beginner-friendly features, free usage, and simple management. The free version allows for 5 feeds and 30 messages per minute, with the option to upgrade for a fee. Adafruit requires minimal coding on the back-end, which made it simple to make a front-end client for my project. I also implemented webhooks to send messages to Discord, which is a really neat feature that is available on Adafruit.

# The Code
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

#### Explanation of `main.py`:
The code is **commented thoroughly** on GitHub. The structure of the program is as follows:
1. [IMPORT LIBRARIES](https://github.com/vurg/stroller-iot/blob/fdb8bd8e2c3de49ec7f4858efcb1c103f6972ef6/main.py#L5C1-L12C58) - import external libraries that we depend on
2. [CONFIGURE PINS](https://github.com/vurg/stroller-iot/blob/fdb8bd8e2c3de49ec7f4858efcb1c103f6972ef6/main.py#L14C1-L29C57) - initialize pins for DHT, LEDs, button, tilt sensor, IR transmitter/receiver
3. [DEFINE SENSOR PREFERENCES](https://github.com/vurg/stroller-iot/blob/fdb8bd8e2c3de49ec7f4858efcb1c103f6972ef6/main.py#L31C1-L50C63) - variables and constants we will be using throughout program
4. [DEFINE CONNECTIVITY SETTINGS](https://github.com/vurg/stroller-iot/blob/fdb8bd8e2c3de49ec7f4858efcb1c103f6972ef6/main.py#L52C1-L66C1) - variables and constants for Wi-Fi and MQTT connections
5. [DEFINE FUNCTIONS](https://github.com/vurg/stroller-iot/blob/fdb8bd8e2c3de49ec7f4858efcb1c103f6972ef6/main.py#L67C1-L216C5) - such as sensor read/write functions and helper methods
6. [SETUP](https://github.com/vurg/stroller-iot/blob/fdb8bd8e2c3de49ec7f4858efcb1c103f6972ef6/main.py#L218C1-L234C1) - runs once, we connect to Wi-Fi network and MQTT broker and start subscriptions
7. [LOOP](https://github.com/vurg/stroller-iot/blob/fdb8bd8e2c3de49ec7f4858efcb1c103f6972ef6/main.py#L235C1-L286C44) - runs forever, until unhandled exception and crash, or power loss

We can briefly discuss the IR sensor/transmitter logic (below), since the DHT11 is straight-forward:

```
# Preferences for IR Transmitter/Receiver
FREQUENCY = 38000        # Infrared carrier frequency (38 kHz)
PULSE_WIDTH = 26         # Half of the carrier wave period (in microseconds)
ir_signal_count = 0      # Variable to count received IR signals
SIGNAL_COUNT_CUTOFF = 30 # Number of IR signals needed to activate indicator

# Functions to publish IR sensor
def send_IR_sensor():
    try:
        client.publish(topic=AIO_IR_SENSOR_FEED, msg="You bumped into someone!")
        print("DONE")
    except Exception as e:
        print("FAILED")

# Function to encode IR transmitter data using NEC protocol
def encode_nec(data):
    # Start bit
    send_pulse(True)

    # Data bits
    for i in range(8):
        bit = (data >> i) & 1
        send_pulse(bit)

    # Inverted data bits
    for i in range(8):
        bit = (data >> i) & 1
        send_pulse(not bit)

    # Stop bit
    send_pulse(False)

# Function to send a pulse with the specified value
def send_pulse(value):
    ir_transmitter.on()
    time.sleep_us(PULSE_WIDTH if value else PULSE_WIDTH * 3)
    ir_transmitter.off()
    time.sleep_us(PULSE_WIDTH if value else PULSE_WIDTH * 3)
```



```
# SETUP
# Try WiFi Connection
try:
    ip = do_connect()
except KeyboardInterrupt:
    print("Keyboard interrupt")

# Use the MQTT protocol to connect to Adafruit IO
client = MQTTClient(AIO_CLIENT_ID, AIO_SERVER, AIO_PORT, AIO_USER, AIO_KEY)

# Subscribed messages will be delivered to this callback
client.set_callback(sub_cb)
client.connect()
client.subscribe(AIO_LIGHTS_FEED) #subscribe to lights feed which toggles ON/OFF RGB LED
print("Connected to %s, subscribed to %s topic" % (AIO_SERVER, AIO_LIGHTS_FEED))
```


```
# LOOP
try:  # Code between try: and finally: may cause an error
      # so ensure the client disconnects the server if
      # that happens.
      
    while True:  # Repeat this loop forever
        
        #Check MQTT messages and publish sensor values to MQTT message broker
        client.check_msg()  # Action a message if one is received. Non-blocking.
        send_temperature()  # Publish temperature
        send_humidity()     # Publish humidity

        # IR Transmitter - send pulse if button is pressed
        if not button.value():
            # Button is pressed, send IR signal with encoded message
            encode_nec(0x55)  # Example message (change as needed)
        elif button.value() and ir_signal_count > 0:
            # Button is released, reset IR signal count
            ir_signal_count = 0
        
        # IR Receiver - count number of pulses (counting low to high transitions during button press)
        if not ir_receiver.value():
            # IR signal received
            ir_signal_count += 1
            print("IR signal received:", ir_signal_count)
            while not ir_receiver.value():  # Wait until the IR receiver input goes high
                pass  # Do nothing
        
        # Check criteria that determines if we have bumped into another friendly stroller
        if ir_signal_count > SIGNAL_COUNT_CUTOFF:
            if rgb_isEnabled:
                rgb_led.on()                       # Turn on RGB LED if enabled
            last_rgb_flash_ticks = time.ticks_ms() # Reset RGB led timing
            
            send_IR_sensor()                       # Send MQTT message "You bumped into someone" to Adafruit and discord
            
            while (time.ticks_ms() - last_rgb_flash_ticks) < RGB_INTERVAL:
                pass                               # Do nothing while LED flashes for 10 seconds
            rgb_led.off()                          # Turn off RGB LED
            
        # Turn on the on-board LED when we detect vibrations (using tilt switch for this purpose!) 
        if tilt_pin.value():
            #print("Tilt switch is in the open position")
            led.off()  # Turn off the on-board LED
        else:
            #print("Tilt switch is in the closed position")
            led.on()  # Turn on the on-board LED

finally:  # If an exception is thrown ...
    client.disconnect()  # ... disconnect the client and clean up.
    client = None
    print("Disconnected from Adafruit IO.")
```
The code implements an IR transmitter and receiver to detect proximity events between two strollers. When the button is pressed, the code sends an IR signal with an encoded message using the NEC protocol. The IR receiver part of the code counts the number of received pulses (low to high transitions) during the button press. This is likely to occur when two strollers are within 10 meters of each other, which is the maximum range of the IR transmitter.

When the number of IR signals received exceeds the specified cutoff value (`SIGNAL_COUNT_CUTOFF`), it indicates a proximity event. In response, the code activates the RGB LED indicator (if enabled). It sends an MQTT message to Adafruit IO and Discord: "You bumped into someone!" using the `send_IR_sensor()` function. The RGB LED then flashes for a specific duration (`RGB_INTERVAL`). The RGB LED can be toggled on/off from the Adafruit IO Dashboard, through the lights MQTT topic which the Pico subscribes to.

Another quirk of the code is that I used the tilt sensor to detect vibrations. When the stroller goes over rough surfaces, it lights up the on-board LED on the Pico PCB. This is quite appealing visually.

# Transmitting the data / connectivity
* Temperature and humidity measurements are published  **every minute**. 
* IR sensor measurements are published in **real-time**, whenever our stroller detects another stroller. 

Adafruit.io has built in actions using **webhooks** that send discord messages. For this, you need to create a discord server and go into settings->integrations to obtain webhooks link. Adafruit notifies us on discord whenever we encounter another friendly stroller. Secondly, we are alerted when the temperature or humidity are much higher than our desired range. To achieve all this, my project uses **Wi-Fi** and **MQTT**. I setup the Wi-Fi network as a mobile phone hotspot. Once Wi-Fi connection is established, we establish a connection to the MQTT cloud broker that is hosted on the Adafruit IO server. We can then publish and subscribe messages to different topics, which are called feeds in the Adafruit control panel. We publish to three different feeds (temperature, humidity, and ir-sensor). We subscribe to messages on the lights feed. Toggling on/off the RGB LED on the Adafruit dashboard sends ON/OFF messages to the Pico, which are then parsed to enable/disable the RGB LED. Recall that the RGB multicolor LED turns on whenever our stroller detects another stroller. We recognize some users may not want this feature (unwanted attention).

Wi-Fi and LoRa are wireless protocols with different characteristics. LoRa is designed for long-range, low-power communications in IoT applications, offering excellent outdoor coverage but limited bandwidth and higher latency. Wi-Fi, on the other hand, provides higher data rates and lower latency, making it suitable for applications that require faster communication and higher bandwidth in local area networks. Wi-Fi typically performs well in indoor environments, due to its higher frequency range and ability to penetrate walls and obstacles. Wi-Fi routers are available in indoor and outdoor urban environments, as well as through Wi-Fi hotspots from mobile phones, providing reliable coverage and connectivity. LoRaWAN coverage is limited indoors and limited in some rural areas. This makes Wi-Fi a suitable choice for our Stroller IoT application, because the stroller may be used inside shopping malls, and other indoor spaces. Charging batteries is not a problem for parents with usual child-care routines.

**Note:** The Raspberry Pi Pico W Wi-Fi component is unable to connect to 5G networks!!

# Presenting the data

![](https://hackmd.io/_uploads/BkoBMHfth.png)

The data is published and saved to Adafruit every minute when the device is powered on. Each feed in Adafruit stores the data for 30 days. Webhooks warnings are sent to Discord when temperature is above 26 degC, and humidity is above 70%. The RGB LED feature can also be turned ON or OFF through the Adafruit dashboard. There is also a running text stream that keeps a note of when we bump into someone.


The dashboard is built using feeds and actions, as shown below.
![](https://hackmd.io/_uploads/rkJDGrMY2.png)
![](https://hackmd.io/_uploads/HJSvGBzY2.png)

As an alternative, I tried HiveMQ (encrypted cloud broker), and was able to have an SSL/TLS encrypted connection. If I had more time, I would have tried to built my own back-end with this, and a mobile app to go with it. I plan to try out the TIG stack later this week, because I am interested in learning InfluxDB (time-series database) and Grafana for visualization. 

# Finalizing the design
Overall, I think the Stroller IoT project went well. The first prototype is shown below. During the upcoming days, I will organize the breaboard better by using wires instead of cables. I also plan to make a PCB for it and a 3D-printed, waterproof case. I am nonetheless a bit disappointed that I did not get to use LoRaWAN in my final design. My original goal was to try and use [LoRaWAN with Geolocation](https://backend.orbit.dtu.dk/ws/portalfiles/portal/130478296/paper_final_2.pdf).  I purchased the LoRaWAN antenna, but realized rather late in my project that I would need another antenna (and another device!) to test out proximity detection features. Lack of LoRaWAN coverage was another limitation. Therefore, I had to be clever and used an IR transmitter/sensor for proximity detection. Since I only had one device, the designed prototype had to detect reflected IR signals from self, in addition to other friendly strollers. This is actually more difficult to implement than having two or more devices communicating with each other. The final version of the project should also implement dynamic IR encoding to maximize privacy, and should minimize interference from other IR transmitting devices (including self). Lastly, I will make a mobile app for this. :slightly_smiling_face:
| Prototype with Breadboard + Powerbank| IoT Dashboard |
| -------- | -------- | 
|<img src="https://hackmd.io/_uploads/ryK3T-Mt3.jpg" width="60%" height="60%">|<img src="https://hackmd.io/_uploads/BkoBMHfth.png" width="150%" height="150%">|

**Discord**
![](https://hackmd.io/_uploads/B1Q6WHMF3.png)

**GitHub**: https://github.com/vurg/stroller-iot/tree/main

**HackMD**: https://github.com/vurg/stroller-iot

# Stroller IoT project: https://hackmd.io/@rIFCcdNpR2WfEEjApaiQyw/B1Un8bGFn
# Nasit Vurgun, Software Engineering at Gothenburg University
# Coursework: LNU - Internet of Things (Summer 2023)

import time                   # Allows use of time.sleep() for delays
from mqtt import MQTTClient   # For use of MQTT protocol to talk to Adafruit IO
import ubinascii              # Conversions between binary data and various encodings
import machine                # Interfaces with hardware components
import micropython            # Needed to run any MicroPython code
import random                 # Random number generator
from machine import Pin       # Define pin
from secrets import secrets   # Import secrets for Wi-Fi
import dht                    # Import DHT sensor library

# CONFIGURING PINS
# Initialize DHT11 temperature and humidity sensor
dhtSensor = dht.DHT11(Pin(17))

# Initialize LED pins
green_led = Pin(1, Pin.OUT)  # green LED pin
yellow_led=Pin(2, Pin.OUT)   # yellow LED pin
red_led = Pin(3, Pin.OUT)    # red LED pin
rgb_led = Pin(16, Pin.OUT)   # RGB LED pin
led = Pin("LED", Pin.OUT)    # on-board led pin initialization for Raspberry Pi Pico W

# Initialize button sensor, tilt sensor, IR receiver and transmitter pins
tilt_pin = Pin(0, Pin.IN)              # Tilt sensor PIN (we use it to measure vibrations!)
button = Pin(18, Pin.IN, Pin.PULL_UP)  # Push button PIN
ir_transmitter = Pin(19, Pin.OUT)      # IR transmitter PIN
ir_receiver = Pin(20, Pin.IN)          # IR receiver PIN

# SENSOR PREFERENCES
# Preferences for IR Transmitter/Receiver
FREQUENCY = 38000        # Infrared carrier frequency (38 kHz)
PULSE_WIDTH = 26         # Half of the carrier wave period (in microseconds)
ir_signal_count = 0      # Variable to count received IR signals
SIGNAL_COUNT_CUTOFF = 30 # Number of IR signals needed to activate indicator

# Preferences for measurements and MQTT publishing intervals
TEMPERATURE_INTERVAL = 60000  # Measure temperature interval
HUMIDITY_INTERVAL = 60000     # Measure humidity interval
RGB_INTERVAL = 10000          # How long RGB LED should light up after you bump into another stroller
last_temperature_sent_ticks = 0
last_humidity_sent_ticks = 0
last_rgb_flash_ticks = 0
rgb_isEnabled = True          # Whether RGB LED is enabled

# Preferences for Temperature and Humidity Indicator LEDs
TEMP_LOW = 22.0               # red LED turns on below this, otherwise green LED is on
TEMP_HIGH = 26.0              # red LED turns on above this, otherwise green LED is on
HUMID_HIGH = 70.0             # yellow LED turns on above this

# CONNECTIVITY SETTINGS
# Wi-Fi configuration
WIFI_SSID, WIFI_PASS = secrets["ssid"], secrets["password"]

# MQTT configuration with Adafruit IO (AIO)
AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_USER = "stroller"
AIO_KEY = secrets["ada_key"]
AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id())  # Can be anything
AIO_LIGHTS_FEED = "stroller/feeds/lights"
AIO_TEMPERATURE_FEED = "stroller/feeds/temperature"
AIO_HUMIDITY_FEED = "stroller/feeds/humidity"
AIO_IR_SENSOR_FEED = "stroller/feeds/ir-sensor"

# FUNCTIONS
# Function to connect Pico to the WiFi
def do_connect():
    import network
    from time import sleep
    import machine
    wlan = network.WLAN(network.STA_IF)         # Put modem on Station mode

    if not wlan.isconnected():                  # Check if already connected
        print('connecting to network...')
        wlan.active(True)                       # Activate network interface
        # set power mode to get WiFi power-saving off (if needed)
        wlan.config(pm = 0xa11140)
        wlan.connect(WIFI_SSID, WIFI_PASS)  # Your WiFi Credential
        print('Waiting for connection...', end='')
        # Check if it is connected otherwise wait
        while not wlan.isconnected() and wlan.status() >= 0:
            print('.', end='')
            sleep(1)
    # Print the IP assigned by router
    ip = wlan.ifconfig()[0]
    print('\nConnected on {}'.format(ip))
    return ip 

# Callback Function to respond to ON/OFF messages from Adafruit IO with RGB LED
def sub_cb(topic, msg):          # sub_cb means "callback subroutine"
    global rgb_isEnabled
    print((topic, msg))          # Outputs the message that was received. Debugging use.
    if msg == b"ON":             # If message says "ON" ...
        rgb_isEnabled = True     # ... then RGB LED on
        print(rgb_isEnabled)
    elif msg == b"OFF":          # If message says "OFF" ...
        rgb_isEnabled = False    # ... then RGB LED off
        print(rgb_isEnabled)
    else:                        # If any other message is received ...
        print("Unknown message") # ... do nothing but output that it happened.

# Function to measure temperature
def measure_temperature():
    try:
        # Measure temperature and humidity
        dhtSensor.measure()
        temperature = dhtSensor.temperature()
        return temperature
    except:
        # Error occurred while reading sensor values
        print("Error in reading sensor values")

# Function to measure humidity
def measure_humidity():
    try:
        # Measure temperature and humidity
        dhtSensor.measure()
        humidity = dhtSensor.humidity()
        return humidity
    except:
        # Error occurred while reading sensor values
        print("Error in reading sensor values")

# Function to publish IR sensor when you meet another friendly stroller
def send_IR_sensor():
    try:
        client.publish(topic=AIO_IR_SENSOR_FEED, msg="You bumped into someone!")
        print("DONE")
    except Exception as e:
        print("FAILED")

# Function to publish temperature
def send_temperature():
    global last_temperature_sent_ticks
    global TEMPERATURE_INTERVAL

    if (time.ticks_ms() - last_temperature_sent_ticks) < TEMPERATURE_INTERVAL:
        return  # Too soon since the last one was sent.

    temperature = measure_temperature()  # Call the measure_temperature() function to get the temperature value.
    handle_temperature(temperature)      # Call function to turn on green or red LED according to temperature preferences
    print("Publishing: {0} to {1} ... ".format(temperature, AIO_TEMPERATURE_FEED), end='')

    try:
        client.publish(topic=AIO_TEMPERATURE_FEED, msg=str(temperature))
        print("DONE")
    except Exception as e:
        print("FAILED")
    finally:
        last_temperature_sent_ticks = time.ticks_ms()

# Function to publish humidity
def send_humidity():
    global last_humidity_sent_ticks
    global HUMIDITY_INTERVAL

    if (time.ticks_ms() - last_humidity_sent_ticks) < HUMIDITY_INTERVAL:
        return  # Too soon since the last one was sent.

    humidity = measure_humidity()  # Call the measure_humidity() function to get the humidity value.
    handle_humidity(humidity)      # Call function to turn on yellow LED according to humidity preferences
    print("Publishing humidity: {0} to {1} ... ".format(humidity, AIO_HUMIDITY_FEED), end='')

    try:
        client.publish(topic=AIO_HUMIDITY_FEED, msg=str(humidity))
        print("DONE")
    except Exception as e:
        print("FAILED")
    finally:
        last_humidity_sent_ticks = time.ticks_ms()

# Function to turn on red or green LED based on temperature preferences
def handle_temperature(temperature):
    # Check if temperature is between 22.0 and 26.0
    if TEMP_LOW <= temperature <= TEMP_HIGH:
        green_led.on()  # Turn on the green LED
        red_led.off()  # Turn off the red LED
    else:
        green_led.off()  # Turn off the green LED
        red_led.on()  # Turn on the red LED

# Function to turn on yellow LED based on humidity preferences
def handle_humidity(humidity):
    # Check if humidity is above 70.0
    if humidity > HUMID_HIGH:
        yellow_led.on()  # Turn on the yellow LED
    else:
        yellow_led.off()  # Turn off the yellow LED

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

import RPi.GPIO as GPIO
import time
import threading
from flask import Flask
from pythonosc import udp_client

# Initialize the Flask app
app = Flask(__name__)

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin you want to use
GPIO_PIN = 17

# Set up the GPIO pin as an input with pull-up resistor
GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Create an OSC client to send commands to your OSC-enabled device. Change IP Address accordingly. 
osc_client = udp_client.SimpleUDPClient("192.168.1.41", 8000)  # Replace with >

# Define a function to handle GPIO events
def gpio_event(channel):
    if GPIO.input(GPIO_PIN) == GPIO.LOW:
        print("Sensor triggered")
        osc_client.send_message("/unity", 1.0)  # Send a float value of 1
    else:
        print("Sensor not triggered")


# Add an event listener for GPIO 17
GPIO.add_event_detect(GPIO_PIN, GPIO.BOTH, callback=gpio_event, bouncetime=100)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)



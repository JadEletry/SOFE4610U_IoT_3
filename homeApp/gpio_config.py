import RPi.GPIO as GPIO
import time

LED_PIN = 21  # Change this to your LED pin number
LDR_PIN = 23  # Change this to your LDR pin number

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LDR_PIN, GPIO.IN)

def light_on():
    GPIO.output(LED_PIN, GPIO.HIGH)
    print("LED turned ON")

def light_off():
    GPIO.output(LED_PIN, GPIO.LOW)
    print("LED turned OFF")

def auto_mode():
    while True:
        ldr_value = GPIO.input(LDR_PIN)
        if ldr_value == GPIO.HIGH:  # Adjust the condition based on your LDR readings
            light_on()
        else:
            light_off()
        time.sleep(0.5)  # Adjust the delay as needed
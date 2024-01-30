import RPi.GPIO as GPIO
import time

led_pin1 = 4
led_pin2 = 5
led_pin3 = 6

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)
GPIO.setup(led_pin3, GPIO.OUT)

def RGB_color(color):
	if color == "red":
		GPIO.output(led_pin1, True)
		GPIO.output(led_pin2, False)
		GPIO.output(led_pin3, False)
	elif color == "green":
		GPIO.output(led_pin1, False)
		GPIO.output(led_pin2, True)
		GPIO.output(led_pin3, False)
	elif color == "blue":
		GPIO.output(led_pin1, False)
		GPIO.output(led_pin2, False)
		GPIO.output(led_pin3, True)

for i in range(20):
	RGB_color("red")
	time.sleep(0.5)
	RGB_color("green")
	time.sleep(0.5)
	RGB_color("blue")
	time.sleep(0.5)
except KeyboardInterrupt:
	pass
GPIO.cleanup()

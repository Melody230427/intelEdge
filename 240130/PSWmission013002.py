import RPi.GPIO as GPIO
import time

led_pin = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin, GPIO.OUT)

pwm = GPIO.PWM(led_pin, 300)

print("1.LED 켜기\n2.LED 끄기\n
			3.LED 3초간 점점 밝기\n4.LED 3초간 점점 어둡기\n5.LED 3초간 점점 밝다가 3초간 점점 어둡기\n
			6.원하는 초 입력\n
			입력한 초 동안 점점 밝아지다가 어두워지기\n")
num = input()

if num == 1:
    GPIO.output(led_pin, True)
if num == 2:
    GPIO.output(led_pin, False)
if num == 3:
	pwm.start(0)
	for t_high in range(0, 301, 1):
		pwm.ChangeDutyCycle(t_high)
		time.sleep(0.01)
if num == 4:
	for t_high in range(300, -1, -1):
		pwm.ChangeDutyCycle(t_high)
		time.sleep(0.01)
if num == 5:
	pwm.start(0)
	for t_high in range(0, 301, 1):
		pwm.ChangeDutyCycle(t_high)
		time.sleep(0.01)
	for t_high in range(300, -1, -1):
		pwm.ChangeDutyCycle(t_high)
		time.sleep(0.01)
if num == 6:
	num2 = input("원하는 시간초를 입력하시오 : ")
	pwm.start(0)
    for t_high in range(0, num2*100, 1):
        pwm.ChangeDutyCycle(t_high)
        time.sleep(0.01)
    for t_high in range(num2*100, -1, -1):
		pwm.ChangeDutyCycle(t_high)
		time.sleep(0.01)
	
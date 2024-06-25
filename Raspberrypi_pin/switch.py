import RPi.GPIO as GPIO
relay_con = 23
button_in = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_con,GPIO.OUT)
GPIO.setup(button_in,GPIO.IN,pull_up_down = GPIO.PUD_UP)

while True:
  if GPIO.input(button_in) == 0:
    print("button was pressed")

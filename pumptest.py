import RPi.GPIO as GPIO
import time

# GPIO-Modus auf BOARD setzen
GPIO.setmode(GPIO.BOARD)

# Pin 11 als Ausgang festlegen
GPIO.setup(11, GPIO.OUT)

# Pin 11 auf HIGH setzen
GPIO.output(11, GPIO.HIGH)

# 5 Sekunden warten
time.sleep(5)

# Pin 11 auf LOW setzen, um den Zustand zurückzusetzen
GPIO.output(11, GPIO.LOW)

# GPIO sauber freigeben
GPIO.cleanup()

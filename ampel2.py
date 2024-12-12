import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BOARD)


RED_PIN = 11    
YELLOW_PIN = 13 
GREEN_PIN = 15 


GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(YELLOW_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)


def traffic_light_sequence():
    while True:
        
        GPIO.output(RED_PIN, GPIO.HIGH)  # Rot an
        GPIO.output(YELLOW_PIN, GPIO.LOW)  # Gelb aus
        GPIO.output(GREEN_PIN, GPIO.LOW)  # Grün aus
        sleep(7)  # 7 Sekunden Rot

        # Rot-Gelb Phase
        GPIO.output(RED_PIN, GPIO.HIGH)  # Rot an
        GPIO.output(YELLOW_PIN, GPIO.HIGH)  # Gelb an
        GPIO.output(GREEN_PIN, GPIO.LOW)  # Grün aus
        sleep(2)  # 2 Sekunden Rot+Gelb

        # Grün Phase
        GPIO.output(RED_PIN, GPIO.LOW)  # Rot aus
        GPIO.output(YELLOW_PIN, GPIO.LOW)  # Gelb aus
        GPIO.output(GREEN_PIN, GPIO.HIGH)  # Grün an
        sleep(5)  # 5 Sekunden Grün

        # Gelb Phase
        GPIO.output(RED_PIN, GPIO.LOW)  # Rot aus
        GPIO.output(YELLOW_PIN, GPIO.HIGH)  # Gelb an
        GPIO.output(GREEN_PIN, GPIO.LOW)  # Grün aus
        sleep(2)  # 2 Sekunden Gelb


try:
    traffic_light_sequence()
except KeyboardInterrupt:
    print("Programm beendet.")
finally:
    GPIO.cleanup() 
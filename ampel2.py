import RPi.GPIO as GPIO
from time import sleep

# Setze die GPIO-Nummerierung auf BCM
GPIO.setmode(GPIO.BCM)

# Definiere die Pins für rot, gelb und grün
RED_PIN = 17    # Pin 11 in BCM
YELLOW_PIN = 27 # Pin 13 in BCM
GREEN_PIN = 22  # Pin 15 in BCM

# Setze die Pins als Ausgang
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(YELLOW_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)

# Funktion für die Ampelphasen
def traffic_light_sequence():
    while True:
        # Rot Phase
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

# Start der Ampelsequenz
try:
    traffic_light_sequence()
except KeyboardInterrupt:
    print("Programm beendet.")
finally:
    GPIO.cleanup()  # Sicherstellen, dass alle GPIO-Pins freigegeben werden
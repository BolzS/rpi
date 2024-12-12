# Bibliotheken laden
from gpiozero import TrafficLights
from time import sleep

# Initialisierung der Ampel mit physischen Pins (Pin 11 = Rot, Pin 13 = Gelb, Pin 15 = Grün)
# Beachte: gpiozero verwendet die BOARD-Nummerierung, nicht BCM
lights = TrafficLights(11, 13, 15, pin_factory=None)

# Definition einer Funktion für die Ampelphasen
def traffic_light_sequence():
    while True:
        # Rot-Phase
        lights.red.on()
        lights.yellow.off()
        lights.green.off()
        sleep(7)

        # Rot-Gelb-Phase
        lights.red.on()
        lights.yellow.on()
        lights.green.off()
        sleep(2)

        # Grün-Phase
        lights.red.off()
        lights.yellow.off()
        lights.green.on()
        sleep(5)

        # Gelb-Phase
        lights.red.off()
        lights.yellow.on()
        lights.green.off()
        sleep(2)

# Aufruf der Steuerung für die Ampelphasen
traffic_light_sequence()

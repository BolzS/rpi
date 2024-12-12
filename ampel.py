# Bibliotheken laden
from gpiozero import TrafficLights
from time import sleep

# Initialisierung von GPIO25, GPIO8 und GPIO7 als Ampel (Ausgang)
lights = TrafficLights(11, 13, 15)

# Definition einer Funktion für die Ampelphasen
def traffic_light_sequence():
    # Wiederholung einleiten
    while True:
        # Rot-Phase
        yield (1, 0, 0)
        sleep(7)
        # Rot-Gelb-Phase
        yield (1, 1, 0) # rot+gelb
        sleep(2)
        # Grün-Phase
        yield (0, 0, 1) # grün
        sleep(5)
        # Gelb-Phase
        yield (0, 1, 0) # gelb
        sleep(2)

# Aufruf der Steuerung für die Ampelphasen
lights.source = traffic_light_sequence()
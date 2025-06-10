from sensor import Sensor
from display import Display

class CarPark:
    pass

    def __init__(self, location="unknown", capacity=0, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []

    def __str__(self):
        return f"Welcome to {self.location} car park. {self.capacity} bays are available."



    def register(self, component):
        "Registers components of a car park."
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        if isinstance (component, Sensor):
            self.sensors.append(component)
        elif isinstance (component, Display):
            self.displays.append(component)
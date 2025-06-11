from abc import ABC, abstractmethod

import random

class CarPark:
    pass

class Sensor(ABC):
    """Provides sensors to detect cars"""
    def __init__(self, id, car_park=None, is_active=False):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        status = "is active" if self.is_active else "not active"
        return f"{self.id}: Sensor {status}"

    @abstractmethod
    def update_car_park(self, plate):
        pass

    def _scan_plate(self):
        return random.choice(self.car_park.plates)

    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate)

class EntrySensor(Sensor):
    def update_car_park(self, plate):
       self.car_park.add_car(plate)
       print(f"Incoming 🚘 vehicle detected. Plate: {plate}")

class ExitSensor(Sensor):
    def update_car_park(self, plate):
       self.car_park.remove_car(plate)
       print(f"Outgoing 🚗 vehicle detected. Plate: {plate}")
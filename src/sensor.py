from abc import ABC, abstractmethod

import random

class CarPark:
    def __init__(self):
        self.plates = []

    def add(self, plate):
        self.plates.append(plate)

    def remove_car(self, plate):
        if plate in self.plates:
            self.plates.remove(plate)

class Sensor(ABC):
    """Provides sensors to detect cars"""
    def __init__(self, id, car_park=None, is_active=False):
        "initalise a sensor"
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        "Return a string representation of the sensor"
        status = "is active" if self.is_active else "not active"
        return f"{self.id}: Sensor {status}"

    @abstractmethod
    def update_car_park(self, plate):
        "Abstract method to update the car park"
        pass

    def detect_vehicle(self):
        "Simualte detection of cars and update the car park"
        plate = self._scan_plate()
        self.update_car_park(plate)

class EntrySensor(Sensor):
    """Sensor that detects incoming cars entering the car park
    """
    def update_car_park(self, plate):
        """Add the  detected car plate to the car park
        """
        print(f"\nIncoming 🚘 vehicle detected. Plate: {plate}")
        self.car_park.add_car(plate)


class ExitSensor(Sensor):
    """Sensor that detects cars exiting the car park"""
    def _scan_plate(self):
        """Simulates scanning a plate of a car leaving by randomly choosing one"""
        if not self.car_park.plates:
            print("No plates detected")
            return None
        return random.choice(self.car_park.plates)

    def update_car_park(self, plate):
        """Remove the detected car plate from the car pork"""
        print(f"\nOutgoing 🚗 vehicle detected. Plate: {plate}")
        self.car_park.remove_car(plate)

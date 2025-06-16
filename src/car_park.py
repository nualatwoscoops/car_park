from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime

class CarPark:
    def __init__(self, location="unknown", capacity=0, plates=None, sensors=None, displays=None, temperature=25, log_file=Path("log.txt")):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        self.temperature = temperature
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)

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

    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays()
        self._log_car_activity(plate, "exited")

    def update_displays(self):
        for display in self.displays:
            display.update(data = {"available_bays": self.available_bays, "temperature": self.temperature})
            print(f"Updating: {display}")

    @property
    def available_bays(self):
        #car_park.available_bays
        calculated_available_bays = self.capacity - len(self.plates)
        if calculated_available_bays < 0:
            return 0
        else:
            return calculated_available_bays


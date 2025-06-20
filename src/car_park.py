import json
from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime

class CarPark:
    """Represents a car park with location, capactily, list of cars, sensors,
    displays, and logging capabilities."""

    def __init__(self, location="unknown", capacity=0, plates=None, sensors=None, displays=None, temperature=25, log_file=Path("log.txt"), config_file=Path("config.json")):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        self.temperature = temperature
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)
        self.config_file = Path(config_file)

    def __str__(self):
        return f"Welcome to {self.location} Car Park. {self.available_bays} of {self.capacity} bays are available."

    def register(self, component):
        "Registers components of a car park."
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        if isinstance (component, Sensor):
            self.sensors.append(component)
        elif isinstance (component, Display):
            self.displays.append(component)

    def _log_car_activity(self, plate, action):
        "Logs car entry and exit activity to the log file"
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")

    def add_car(self, plate):
        "Add car plates to the car park log and update displays"
        self.plates.append(plate)
        self.update_displays()
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        "Removes car plates from update displays and adds instance to the car park log"
        self.plates.remove(plate)
        self.update_displays()
        self._log_car_activity(plate, "exited")

    def update_displays(self):
        "Notify displays to update their information"
        for display in self.displays:
            display.update(
                {"\nAvailable Bays": self.available_bays,
                 "\nTemperature": self.temperature,
            })
            #print(f"\nUpdating: {display}")

    @property
    def available_bays(self):
        "Calculate number of bays available"
        #car_park.available_bays
        calculated_available_bays = self.capacity - len(self.plates)
        if calculated_available_bays < 0:
            return 0
        else:
            return calculated_available_bays

    def write_config(self):
        "Write current car park configuration data to the config file"
        config_data = {
            "location": self.location,
            "capacity": self.capacity,
            "log_file": str(self.log_file),
            "plates": self.plates,
            "sensors": self.sensors,
            "displays": self.displays,
        }
        with self.config_file.open("w") as f:
            json.dump(config_data, f)

    @classmethod
    def from_config(cls, config_file=Path("config.json")):
        "Creates a CarPark instance from a config file."
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return cls(
            location=config["location"],
            capacity=config["capacity"],
            plates=config.get("plates", []),
            sensors=config.get("sensors", []),
            displays=config.get("displays", []),
            log_file=config.get("log_file", "log.txt"),
            config_file=config_file
        )


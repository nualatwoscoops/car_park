from car_park import CarPark
from pathlib import Path
from sensor import EntrySensor, ExitSensor
from display import Display

#create car park and configure
moondalup_car_park = CarPark(
    location="Moondalup",
    capacity=100,
    log_file="moondalup.txt",
    config_file=Path("moondalup_config.json")
)

print(moondalup_car_park)

#save car park to file
moondalup_car_park.write_config()

#reload the car park from config (like start up)
moondalup_car_park = CarPark.from_config(Path("moondalup_config.json"))

entry_sensor = EntrySensor(id=1, is_active=True, car_park=moondalup_car_park)
exit_sensor = ExitSensor(id=2, is_active=True, car_park=moondalup_car_park)
display_1 = Display(id=1, is_on=True, message="Welcome to Moondalup", car_park=moondalup_car_park)

moondalup_car_park.register(entry_sensor)
moondalup_car_park.register(exit_sensor)
moondalup_car_park.register(display_1)

print("\n--- 🚗 Cars Entering ---")
for i in range(10):
    plate = f"CAR-{i:03}"
    entry_sensor.update_car_park(plate)

print("\n--- 🚙 Cars Exiting ---")
for i in range(2):
    plate = f"CAR-{i:03}"
    exit_sensor.detect_vehicle()
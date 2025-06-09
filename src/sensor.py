class CarPark:
    pass


class Sensor:
    """Provides sensors to detect cars"""
    def __init__(self, id, car_park=None, is_active=False):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        status = "is active" if self.is_active else "not active"
        return f"{self.id}: Sensor {status}"

class EntrySensor(Sensor):
    pass

class ExitSensor(Sensor):
    pass

s1 = EntrySensor(1, None, True)
print(s1)
S2 = ExitSensor(2, None, False)
print(S2)
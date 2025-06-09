from email import message


class CarPark:
    pass

class Display:
    def __init__(self, id, car_park, message="Welcome to the car park.", is_on=False):
        self.id = id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):
        return f"{self.id}: Display is {"is on" if self.is_on else 'is off'}"

d1 = Display(1, None)
print(d1)
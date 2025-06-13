class Display:
    def __init__(self, id, car_park=None, message="Welcome to the car park.", is_on=True):
        self.id = id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):
        return f"Display {self.id} {'is on' if self.is_on else 'is off'}"

    def update(self, data):
        print(f"\nDisplay {self.id} update received:")
        for key, value in data.items():
            print(f"{key}: {value}")
        if "message" in data:
            self.message = data["message"]

d1 = Display(1, None)
print(d1)
d1.update({"available_bays": 10, "temperature": 22})
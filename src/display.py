class Display:
    """
    Display component that shows the status messages of the car park.
    """
    def __init__(self, id, car_park=None, message="Welcome to the car park.", is_on=True):
        """
        Initialize the display component
        """
        self.id = id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):
        """Indicates if the display is on or off"""
        return f"Display {self.id} {'is on' if self.is_on else 'is off'}"

    def update(self, data):
        """Update the display with new data"""
        if self.car_park is not None:
            print(f"\n{self.car_park}")


        print(f"\nDisplay {self.id} update received:")

        for key, value in data.items():
            print(f"{key}: {value}")

        if "message" in data:
            self.message = data["message"]

        print("*" * 30)
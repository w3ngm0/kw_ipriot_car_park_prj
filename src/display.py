class Display:
    """Display class"""

    def __init__(self, id, car_park, message="", is_on=False):
        self.id = id
        self.car_park = car_park
        self.message = message
        self.is_on = is_on

    def __str__(self):
        ...  # Return string containing sensor's id and status

    def update(self, data):
        for key, value in data.items():
            if key == "message":
                self.message = value
            elif key == "is_on":
                self.is_on = value
            else:
                print(f"{key}: {value}")



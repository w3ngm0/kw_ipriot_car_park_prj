class CarPark:
    """CarPark class"""

    def __init__(self, location="Unknown", capacity=0, plates=None, sensors=None,
                 displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []

    def __str__(self):
        ...  # Return a string containing the car park's location and capacity


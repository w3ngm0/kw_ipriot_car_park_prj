from sensor import Sensor
from display import Display
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

    def register(self, component):
        """
        This method will allow car park to register sensors and displays
        """
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)
        else:
            raise TypeError("Object must be a Sensor or Display")

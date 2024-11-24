from sensor import Sensor
from display import Display
from _datetime import datetime  # use for timestamp entries
from pathlib import Path


class CarPark:
    """CarPark class"""

    def __init__(self, location="Unknown", capacity=0, plates=None, sensors=None,
                 displays=None, log_file=Path("log.txt")):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)

        # create file if it doesn't exist:
        self.log_file.touch(exist_ok=True)

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

    # adding property decorator for available bays
    @property
    def available_bays(self):
        """ Calculates the number of available bays in the car park.
        """
        if len(self.plates) < self.capacity:
            return self.capacity - len(self.plates)
        else:
            return 0

    def update_displays(self):

        """Updates  information for available bays, temperature and other information like
        time."""

        data = {"available_bays": self.available_bays,
                "temperature": 25,
                "time": datetime.now()
                }
        for display in self.displays:
            display.update(data)

    def add_car(self, plate):
        self.plates.append(plate)
        self._log_car_activity(plate, "entered") # logging this car entry
        self.update_displays()

    def remove_car(self, plate):
        self.plates.remove(plate)
        self._log_car_activity(plate, "exited")
        self.update_displays()

    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now(): %Y-%m-%d %H:%M:%S}\n")


from abc import ABC, abstractmethod
import random


class Sensor(ABC):
    """
    Constructor method for Sensor class. Inherits from ABC abstract method
    """
    def __init__(self, id, is_active, car_park):
        """
        Initialize the Sensor object

        Args:
            id (str): Unique identifier for the sensor.
            is_active (bool): Sensor's active status.
            car_park (CarPark): Reference to the associated car park.
        """
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        """
        Return string containing sensor's id
        """
        return f"Sensor {self.id}"


    @abstractmethod
    def update_car_park(self, plate):
        """Abstract method"""
        pass

    def _scan_plate(self):
        return 'FAKE-' + format(random.randint(0, 999), "03d")

    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate)


class EntrySensor(Sensor):
    """ A sensor for detecting vehicles entering the car park"""
    def update_car_park(self, plate):
        if self.is_active:
            print(f"Incoming 🚘 vehicle detected. Plate: {plate}")
            self.car_park.add_car(plate)
        else:
            print("Entry sensor is inactive.")


class ExitSensor(Sensor):
    """ A sensor for detecting vehicles exiting the car park"""
    def update_car_park(self, plate):
        if self.is_active:
            print(f"Outgoing 🚗 vehicle detected. Plate: {plate}")
            self.car_park.remove_car(plate)
        else:
            print("Exit sensor is inactive.")

    def _scan_plate(self):
        return random.choice(self.car_park.plates)


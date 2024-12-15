import json
import unittest
from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from pathlib import Path


class TestCarPark(unittest.TestCase):
    """ Test Car Park System
     Unit test for CarPark class and Sensor class
     """

    def setUp(self):
        # Defining log file path explicitly
        self.log_file_path = Path("log.txt")
        if self.log_file_path.exists():
            self.log_file_path.unlink()  # clean the file before running test

        # Initializing car park
        self.car_park = CarPark("123 Example Street", 100)

        # Create Sensor instances
        self.entry_sensor = EntrySensor(1, True, self.car_park)
        self.exit_sensor = ExitSensor(2, True, self.car_park)

    def tearDown(self):
        # Tear down method to clean file after each test
        self.log_file_path.unlink(missing_ok=True)

    def test_car_park_initialized_with_all_attributes(self):
        """ Test car_park Attribute initialization """
        self.assertIsInstance(self.car_park, CarPark)
        self.assertEqual(self.car_park.location, "123 Example Street")
        self.assertEqual(self.car_park.capacity, 100)
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.sensors, [])
        self.assertEqual(self.car_park.displays, [])
        self.assertEqual(self.car_park.available_bays, 100)
        self.assertEqual(self.car_park.log_file, self.log_file_path)

    def test_add_car(self):
        """ Test add_car method"""
        self.car_park.add_car("FAKE-001")
        self.assertEqual(self.car_park.plates, ["FAKE-001"])
        self.assertEqual(self.car_park.available_bays, 99)

    def test_remove_car(self):
        """ Test remove_car method"""
        self.car_park.add_car("FAKE-001")
        self.car_park.remove_car("FAKE-001")
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.available_bays, 100)

    def test_overfill_the_car_park(self):
        """ Test available bays of car"""
        for i in range(100):
            self.car_park.add_car(f"FAKE-{i}")
        self.assertEqual(self.car_park.available_bays, 0)
        self.car_park.add_car("FAKE-100")
        # Overfilling the car park should not change the number of available bays
        self.assertEqual(self.car_park.available_bays, 0)

    # Removing a car from an overfilled car park should not change the number of available bays
        self.car_park.remove_car("FAKE-100")
        self.assertEqual(self.car_park.available_bays, 0)

    def test_removing_a_car_that_does_not_exist(self):
        with self.assertRaises(ValueError):
            self.car_park.remove_car("NO-1")

# Test Cases for Sensor class
    def test_entry_sensor_initialization(self):
        """ Test EntrySensor attribute initialization"""
        self.assertEqual(self.entry_sensor.id, 1)
        self.assertEqual(self.entry_sensor.is_active, True)
        self.assertEqual(self.entry_sensor.car_park, self.car_park)

    def test_exit_sensor_initialization(self):
        """ Test ExitSensor attribute initialization"""
        self.assertEqual(self.exit_sensor.id, 2)
        self.assertEqual(self.exit_sensor.is_active, True)
        self.assertEqual(self.exit_sensor.car_park, self.car_park)

    def test_entry_sensor_detect_vehicle(self):
        """ Test to detect_vehicle for EntrySensor"""
        initial_bays = self.car_park.available_bays
        self.entry_sensor.detect_vehicle()
        self.assertEqual(len(self.car_park.plates), 1)
        self.assertTrue(self.car_park.available_bays < initial_bays)

    def test_exit_sensor_detect_vehicle(self):
        """ Adding car to car park """
        self.car_park.add_car("FAKE-001")

        """Test detect_vehicle for ExitSensor"""
        initial_bays = self.car_park.available_bays
        self.exit_sensor.detect_vehicle()
        self.assertEqual(len(self.car_park.plates), 0)
        self.assertTrue(self.car_park.available_bays > initial_bays)

    # Adding register method
    def test_register_raises_type_error(self):
        # Using the car park object self.car_park = CarPark()
        # Assert registering an invalid component raises a TypeError
        with self.assertRaises(TypeError):
            self.car_park.register("Not a Sensor or Display")

    # Unit test for log.txt

    def test_log_file_created(self):
        """Test if log file is created"""
        new_log_file = Path("log.txt")
        new_carpark = CarPark("123 Example Street", 100, log_file=self.log_file_path)
        self.assertTrue(new_log_file.exists())

    # inside the TestCarPark class
    # inside the TestCarPark class
    def test_car_logged_when_entering(self):
        """Test that a car is logged when it enters"""
        self.car_park.add_car("NEW-001")
        with self.car_park.log_file.open() as f:
            lines = f.readlines()
        # Ensure log file is not empty
        self.assertTrue(lines, "Log file is empty after adding to car.")
        last_line = lines[-1]
        self.assertIn("NEW-001", last_line)  # check plate entered
        self.assertIn("entered", last_line)  # check description
        self.assertIn("\n", last_line)  # check entry has a new line

    def test_car_logged_when_exiting(self):
        """Test that a car is logged when it exits"""
        self.car_park.add_car("NEW-001")
        self.car_park.remove_car("NEW-001")
        with self.car_park.log_file.open() as f:
            lines = f.readlines()
        last_line = lines[-1]
        self.assertIn("NEW-001", last_line)  # check plate entered
        self.assertIn("exited", last_line)  # Check if the action is logged
        self.assertIn("\n", last_line) # check entry has a new line

    def test_car_park_initialized_with_config_file(self):
        """Test CarPark initialization from a config file."""
        # Create a sample config file
        config_file = Path("test_config.json")
        with config_file.open("w") as f:
            f.write('{"location": "Test Location", "capacity": 50, "log_file": "test_log.txt"}')

        # Initialize CarPark
        car_park = CarPark(config_file=config_file)

        # Assertions
        self.assertEqual(car_park.location, "Test Location")
        self.assertEqual(car_park.capacity, 50)
        self.assertEqual(car_park.log_file, Path("test_log.txt"))

        # Clean up
        config_file.unlink(missing_ok=True)

    def test_available_bays(self):
        """Test CarPark and its available bays"""
        # Initial full available bays
        self.assertEqual(self.car_park.available_bays, 100)

        # Add a car to check available bays
        self.car_park.add_car("FAKE-001")
        self.assertEqual(self.car_park.available_bays, 99)
        # Add another
        self.car_park.add_car("FAKE-002")
        self.assertEqual(self.car_park.available_bays, 98)

        # Now remove a car
        self.car_park.remove_car("FAKE-001")
        self.assertEqual(self.car_park.available_bays, 99)


if __name__ == "__main__":
    unittest.main()

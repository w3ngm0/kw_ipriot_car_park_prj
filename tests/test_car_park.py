import unittest
from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from pathlib import Path


class TestCarPark(unittest.TestCase):
    """ Test Car Park System
     Unit test for CarPark class and Sensor class
     """

    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)

        # Create Sensor instances
        self.entry_sensor = EntrySensor(1, True, self.car_park)
        self.exit_sensor = ExitSensor(2, True, self.car_park)

    def tearDown(self):
        # Tear down method to clean file after each test
        Path("new_log.txt").unlink(missing_ok=True)

    def test_car_park_initialized_with_all_attributes(self):
        """ Test car_park Attribute initialization """
        self.assertIsInstance(self.car_park, CarPark)
        self.assertEqual(self.car_park.location, "123 Example Street")
        self.assertEqual(self.car_park.capacity, 100)
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.sensors, [])
        self.assertEqual(self.car_park.displays, [])
        self.assertEqual(self.car_park.available_bays, 100)
        self.assertEqual(self.car_park.log_file, Path("log.txt"))

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
        new_carpark = CarPark("123 Example Street", 100, log_file="new_log.txt")
        self.assertTrue(Path("new_log.txt").exists())

    # inside the TestCarPark class
    # inside the TestCarPark class
    def test_car_logged_when_entering(self):
        new_carpark = CarPark("123 Example Street", 100,
                              log_file="new_log.txt")  # TODO: change this to use a class attribute or new instance variable
        self.car_park.add_car("NEW-001")
        with self.car_park.log_file.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn("NEW-001", last_line)  # check plate entered
        self.assertIn("entered", last_line)  # check description
        self.assertIn("\n", last_line)  # check entry has a new line

    def test_car_logged_when_exiting(self):
        new_carpark = CarPark("123 Example Street", 100,
                              log_file="new_log.txt")  # TODO: change this to use a class attribute or new instance variable
        self.car_park.add_car("NEW-001")
        self.car_park.remove_car("NEW-001")
        with self.car_park.log_file.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn(last_line, "NEW-001")  # check plate entered
        self.assertIn(last_line, "exited")  # check description
        self.assertIn(last_line, "\n")  # check entry has a new line


if __name__ == "__main__":
    unittest.main()

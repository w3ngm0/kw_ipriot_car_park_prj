import unittest
from car_park import CarPark
from sensor import EntrySensor, ExitSensor


class TestCarPark(unittest.TestCase):
    """ Test Car Park System
     Unit test for CarPark class and Sensor class
     """
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)

        # Create Sensor instances
        self.entry_sensor = EntrySensor(1, True, self.car_park)
        self.exit_sensor = ExitSensor(2, True, self.car_park)

    def test_car_park_initialized_with_all_attributes(self):
        """ Test car_park Attribute initialization """
        self.assertIsInstance(self.car_park, CarPark)
        self.assertEqual(self.car_park.location, "123 Example Street")
        self.assertEqual(self.car_park.capacity, 100)
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.sensors, [])
        self.assertEqual(self.car_park.displays, [])
        self.assertEqual(self.car_park.available_bays, 100)

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


if __name__ == "__main__":
    unittest.main()

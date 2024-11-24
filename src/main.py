"""Main Script for Car park System"""
from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display


def main():
    # Initialize car park object according to TODO
    car_park = CarPark(location="moondalup", capacity=100, log_file="moondalup.txt")

    # TODO: create an entry sensor object with id 1, is_active True, and car_park car_park
    entry_sensor = EntrySensor(id=1, is_active=True, car_park=car_park)

    # TODO: create an exit sensor object with id 2, is_active True, and car_park car_park
    exit_sensor = ExitSensor(id=2, is_active=True, car_park=car_park)

    # TODO: create a display object with id 1, message "Welcome to Moondalup", is_on True, and car_park car_park
    display = Display(id=1, message="Welcome to Moondalup", is_on=True, car_park=car_park)

    # Print initial car park details
    print(f"Location: {car_park.location}")
    print(f"Capacity: {car_park.capacity}")
    print(f"Available Bays: {car_park.available_bays}")
    print(f"Log File: {car_park.log_file}")
    print(f"Display Message: {display.message}")

    # TODO: drive 10 cars into the car park (must be triggered via the sensor - NOT by calling car_park.add_car directly)
    print()
    print("----Driving 10 cars into  the car park---")
    for i in range(1, 11):
        entry_sensor.detect_vehicle()
        print(f"Display Message: {display.message}")

    # Print car park details after 10 cars enter
    print(f"\nAvailable Bays after 10 cars entered: {car_park.available_bays}")

    # TODO: drive 2 cars out of the car park (must be triggered via the sensor - NOT by calling car_park.remove_car directly)
    print()
    print("--- Driving 2 cars out of the car park---")
    for i in range(1, 3):
        exit_sensor.detect_vehicle()
        print(f"Display Message: {display.message}")

    # print message after car exit
    print()
    print(f"Available Bays after 2 cars exited: {car_park.available_bays}")


if __name__ == "__main__":
    main()

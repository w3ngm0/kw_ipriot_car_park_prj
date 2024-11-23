# kw_ipriot_car_park_prj

# Car Project 🚗

## Brief Overview
This project is a simplified car park system made using Object-Oriented Programming concepts. 
This system consists of a car park, sensors and a display to track cars entering to occupy 
the parking bays and exiting the parking bays.


## Features
- Car Park: Will contain the nuber of parking bays and their availability.
- Sensors : Use sensor objects to detect a cars movement as it enters and leaves the bay 
- Displays: Will display the number of available parking bays relying on the sensor.


## Installation of Project 
To get started with the project, you can follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/w3ngm0/ipriot_car_park_prj.git


### Images and Additional Evidencing
![Initial commit](images/gh_image.png)


| Class Name   | Attributes                             | Methods                              |
|--------------|----------------------------------------|--------------------------------------|
| `CarPark`    | capacity, available_bays, plates_id    | add_car, remove_car , is_full        |
| `Sensor`     | sensor_id, sensor_position(entry/exit) | detect_car, reset_sensor             |
| `Display`    | message , location (entry or exit)     | show_display, update_display_message |
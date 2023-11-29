# Introduction to Python - BBC course
# 27, 28 and 29 November 2023
# Script by Pilar Tomas
# Trainer: John Hunt
# This script asks the user to enter some temperatures.
# It stops when -1 is entered. Then, it analyses given data series.
# This script requires files readings.py and utils.py

from readings import TemperatureReading
from readings import RainfallReading
from readings import InvalidTemperatureException
from utils import *

# test to verify the module is being run as the main module
# it also adds some exception handling code
if __name__ == "__main__":
    print('Only run if main module')
    try:
        TemperatureReading(13.5, '01/05/20', 'London', 'Celsius') + '5.5'
    except InvalidTemperatureException as e:
        print(e)

continue_to_enter_data = True

readings = []

while continue_to_enter_data:
    input_str = input("Please enter a temperature reading (-1 to end): ")
    while input_str.count('.') > 1 or input_str[len(input_str) - 1] == ".":
        input_str = input("Please enter a correct temperature reading (-1 to end): ")
    else:
        num = input_str.replace('.', '')
        if num.isnumeric():
            input_str = float(input_str)
            readings.append(input_str)
            print(f"You have entered these readings: {readings}")
        elif input_str == '-1':
            input_str = float(input_str)
            readings.append(input_str)
            continue_to_enter_data = False
            len1 = len(readings)
            if len1 == 1:
                print(f"You have entered this reading: {readings}")
                print(f"There is one reading in total.")
            else:
                print(f"You have entered these readings: {readings}")
                print(f"There are {len1} readings in total.")
        else:
            input_str = input("Please enter a correct temperature reading (-1 to end): ")

# sorting the values in the list

print("-" * 8)

readings.sort()
print(f"Temperature readings sorted: {readings}")

readings.reverse()
print(f"Temperature readings in reverse: {readings}")
if readings.count(0.0) == 1:
    print(f'There is one Zero reading.')
else:
    print(f"There are {readings.count(0.0)} Zero readings.")

print("-" * 8)

# creating a copy of the list

readings_copy = readings.copy()
print('Copy of temperature readings:', readings_copy)

readings_copy.append(5.5)

print('Temperature readings:', readings)
print('Copy of Temperature readings:', readings_copy)

print(f'Popping element from end of copy list {readings_copy.pop()}')
print(f'Readings copy now contains {readings_copy}')

print("-" * 25)

# LAB 5: functions

readings = [13.5, 11.1, 17.5, 12.6, 15.3, 12.2, 16.6, 14.6]

print(f"The average temperature value is {average(readings):.2f}")
print(f"The median temperature value is {median(readings):.2f}")

print(f"Min temp in list = {minimum(readings)}")
print(f'Min temp in list start position 4 = {minimum(readings, 3)}')

print(f'Max temp in list = {maximum(readings)}')
print(f'Max temp in list starting position 4 = {maximum(readings, 3)}')

min_temp, max_temp = data_range(readings)

print(f'Range of temperatures from {min_temp} to {max_temp}')
print("-" * 25)

print(f'13.5 celsius as fahrenheit - {celsius_to_fahrenheit(13.5)}')

print(f'56.3 fahrenheit as celsius - {fahrenheit_to_celsius(56.3):.1f}')

print("-" * 25)

# filtering out temperatures over 10.0 and converting them to Fahrenheit

temp = [1.4, 12.1, 4.7, 13.4, 5, 22.3, 2.6, 1.5]

# method 1
result = []

for item in temp:
    if item > 10.0:
        result.append(celsius_to_fahrenheit(item))

print([round(item, 2) for item in result])

# method 2
result = list(
    map(celsius_to_fahrenheit,
        filter(lambda v: v > 10.0,
               temp)))

print([round(item, 2) for item in result])

print("-" * 25)

# LAB 6: higher order functions

# converting list to Fahrenheit

readings = [13.5, 11.1, 17.5, 12.6, 15.3, 12.2, 16.6, 14.6]

fahrenheit_temperatures = list(map(celsius_to_fahrenheit, readings))
print(f'Fahrenheit Temperatures: {[round(item, 2) for item in fahrenheit_temperatures]}')

# filtering out temperatures over 14.0

higher_temperatures = list(
    filter(lambda v: v > 14, readings))

print(f'Temperatures above 14.0: {higher_temperatures}')

# convert temperatures above 14.0 to Fahrenheit

converted_temperatures = list(
    map(celsius_to_fahrenheit, filter(lambda v: v > 14, readings)))

print(f'Fahrenheit Temperatures above 14.0c: '
      f'{[round(item, 2) for item in converted_temperatures]}')

# LAB 7 - Classes

CELSIUS = "Celsius"
FAHRENHEIT = "Fahrenheit"

readings = [
    TemperatureReading(13.5, '01/05/20', 'London',
                       'Celsius'),
    TemperatureReading(12.6, '02/05/20', 'London',
                       'Celsius'),
    TemperatureReading(15.3, '03/05/20', 'London',
                       'Celsius'),
    TemperatureReading(12.2, '04/05/20', 'London',
                       'Celsius'),
    TemperatureReading(16.6, '05/05/20', 'London',
                       'Celsius'),
    TemperatureReading(14.6, '05/05/20', 'London',
                       'Celsius'),
    TemperatureReading(15.6, '05/05/20', 'London',
                       'Celsius')]

temp1 = TemperatureReading(13.5, '01/05/20', 'London', 'Celsius')
print(temp1)

temp2 = temp1.convert()
print(f'temp1: {temp1}')
print(f'temp2: {temp2}')

print("" * 25)

# LAB 8 - Operators

# added some extra methods to TemperatureReading class above

new_temperature = (TemperatureReading(13.5, '01/05/20', 'London', 'Celsius')
                   + TemperatureReading(15.5, '01/05/20','London', 'Celsius'))

print('Adding two temperatures:', new_temperature)

new_temperature = TemperatureReading(13.5, '01/05/20', 'London', 'Celsius') + 5
print('Adding a temperature and an int', new_temperature)

new_temperature = TemperatureReading(13.5, '01/05/20', 'London', 'Celsius') + 5.5
print('Adding a temperature and a float', new_temperature)

another_temperature = TemperatureReading(14.6, '05/05/20',
                                         'London')

print(new_temperature > another_temperature)
print(new_temperature >= another_temperature)
print(new_temperature == another_temperature)
print(new_temperature != another_temperature)
print(new_temperature < another_temperature)
print(new_temperature <= another_temperature)

sorted_data = sorted(readings)
print(sorted_data)

print("-" * 25)

#  LAB 9 - Inheritance
#  Adding root class Reading, and making TemperatureReading extend that.
#  Defining a RainfallReading class that will also extend Reading
#  Adding attributes and methods for both subclasses

rainfall_readings = [
    RainfallReading(2.0, '01/05/20', '11:00', 'London'),
    RainfallReading(2.6, '02/05/20', '11:30', 'London'),
    RainfallReading(2.3, '03/05/20', '11:00', 'London'),
    RainfallReading(3.2, '04/05/20', '12:00', 'London'),
    RainfallReading(1.6, '05/05/20', '10:45', 'London')
]

print('All Rainfall Readings:')
print(*rainfall_readings, sep=", ")

rr1 = RainfallReading(2.0, '01/05/20', '11:00', 'London')
rr2 = RainfallReading(2.3, '03/05/20', '11:00', 'London')
print(rr1 < rr2)
print(rr1 == rr2)
print(rr1 > rr2)

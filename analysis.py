# Introduction to Python - BBC course
# 27, 28 and 29 November 2023
# Script by Pilar Tomas
# Trainer: John Hunt
# This script asks the user to enter some temperatures.
# It stops when -1 is entered, and then it analyses the figures.
# This script draft splits into main.py, utils.py and readings.py

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


def average(data):
    """A simple function to calculate the average"""
    return sum(data) / len(data)


print(f"The average temperature value is {average(readings):.2f}")


def median(data):
    """A simple function to calculate the median"""
    sorted_data = sorted(data)
    data_length = len(data)
    index = (data_length - 1) // 2
    if data_length % 2 == 1:  # checks for an odd number
        return sorted_data[index]
    else:
        return (sorted_data[index] +
                sorted_data[index + 1]) / 2.0


print(f"The median temperature value is {median(readings):.2f}")


def minimum(data,
            position=0):
    """A function that returns the min value in the list"""
    sorted_data = sorted(data)
    return sorted_data[position:][0]


print(f"Min temp in list = {minimum(readings)}")
print(f'Min temp in list start position 4 = {minimum(readings, 3)}')


def maximum(data,
            position=0):
    """A function that returns the max value in the list"""
    sorted_data = sorted(data)
    return sorted_data[position:][-1]


print(f'Max temp in list = {maximum(readings)}')
print(f'Max temp in list starting position 4 = {maximum(readings, 3)}')


def data_range(data):
    """A function that returns the minimum and maximum values in the list"""
    min_temp = minimum(data)
    max_temp = maximum(data)
    return min_temp, max_temp


min_temp, max_temp = data_range(readings)

print(f'Range of temperatures from {min_temp} to {max_temp}')
print("-" * 25)


def celsius_to_fahrenheit(data):
    """A function that converts Celsius to Fahrenheit"""
    return data * 9 / 5 + 32


print(f'13.5 celsius as fahrenheit - {celsius_to_fahrenheit(13.5)}')


def fahrenheit_to_celsius(data):
    return (data - 32) * 5 / 9


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


class Reading:
    """root class of the inheritance hierarchy"""

    def __init__(self, value, date, location):
        self.value = value
        self.date = date
        self.location = location

    def __repr__(self):
        def __repr__(self):
            return f"Reading({self.value}, {self.date}, {self.location})"

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __ne__(self, other):
        return self.value != other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value


class TemperatureReading(Reading):
    """Subclass that represents information for temperature readings"""

    def __init__(self, value, date, location, scale=CELSIUS):
        super().__init__(value, date, location)
        self.scale = scale

    def __repr__(self):
        return (f"TemperatureReading({self.value}, {self.date}, {self.location}, "
                f"{self.scale})")

    def __str__(self):
        return (f"TemperatureReading[{self.scale}]({self.value} "
                f"on {self.date} at {self.location})")

    def convert(self):
        """This method converts Celsius to Fahrenheit and vice-versa"""
        if self.scale == CELSIUS:
            return (f"TemperatureReading[Fahrenheit]({celsius_to_fahrenheit(self.value)} "
                    f"on {self.date} at {self.location})")
        else:
            return (f"TemperatureReading[Celsius]({fahrenheit_to_celsius(self.value)} "
                    f"on {self.date} at {self.location})")

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            new_value = self.value + other
        else:
            new_value = self.value + other.value
        return TemperatureReading(new_value, self.date,
                                  self.location, self.scale)

    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            new_value = self.value - other
        else:
            new_value = self.value - other.value
            return TemperatureReading(new_value, self.date,
                                      self.location, self.scale)


class RainfallReading(Reading):
    """Subclass that represents information for rainfall readings"""

    def __init__(self, value, date, location, time):
        super().__init__(value, date, location)
        self.time = time

    def __repr__(self):
        return (f"RainfallReading({self.value}, {self.date}, "
                f"{self.location}, {self.time})")

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            new_value = self.value + other
        else:
            new_value = self.value + other.value
        return RainfallReading(new_value, self.date,
                               self.location, self.time)

    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            new_value = self.value - other
        else:
            new_value = self.value - other.value
            return RainfallReading(new_value, self.date,
                                   self.location, self.time)


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

# LAB 10 - Modules
# Breaking this script up into main.py, utils.py and readings.py

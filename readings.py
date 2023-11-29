# Introduction to Python - BBC course
# 27, 28 and 29 November 2023
# Script by Pilar Tomas
# Trainer: John Hunt
# This script requires utils.py and defines classes to complement main.py

from utils import *

CELSIUS = "Celsius"
FAHRENHEIT = "Fahrenheit"


class InvalidTemperatureException(ValueError):
    """ Represents an invalid Temperature reading """

    def __init__(self, value, message):
        self.value = value
        self.message = message

    def __str__(self):
        return f'InvalidTemperatureException({self.value}, {self.message})'


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
        elif isinstance(other, TemperatureReading):
            new_value = self.value + other.value
        else:
            # Something is wrong its not an int, a float or a temperature reading
            raise InvalidTemperatureException(other, 'Invalid type for addition to TemperatureReading')
        return TemperatureReading(new_value, self.date, self.location, self.scale)

    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            new_value = self.value - other
        elif isinstance(other, TemperatureReading):
            new_value = self.value - other.value
        else:
            raise InvalidTemperatureException(other, 'Invalid type for subtraction from TemperatureReading')
        return TemperatureReading(new_value, self.date, self.location, self.scale)


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

# LAB 11 - Errors and exceptions
# adding InvalidTemperatureException class
# modifying the __add__ and __sub__ methods so that if the value entered is not an int,
# a float or a TemperatureReading, the InvalidTemperatureException is raised

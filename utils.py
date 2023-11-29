# Introduction to Python - BBC course
# 27, 28 and 29 November 2023
# Script by Pilar Tomas
# Trainer: John Hunt
# This script defines functions to complement main.py

def average(data):
    """A simple function to calculate the average"""
    if isinstance(data[0], int):
        return sum(data) / len(data)
    else:
        raw_data = list(map(lambda v: v, data))
        return sum(raw_data) / len(raw_data)


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


def minimum(data,
            position=0):
    """A function that returns the min value in the list"""
    sorted_data = sorted(data)
    return sorted_data[position:][0]


def maximum(data,
            position=0):
    """A function that returns the max value in the list"""
    sorted_data = sorted(data)
    return sorted_data[position:][-1]


def data_range(data):
    """A function that returns the minimum and maximum values in the list"""
    min_temp = minimum(data)
    max_temp = maximum(data)
    return min_temp, max_temp


def celsius_to_fahrenheit(data):
    """A function that converts Celsius to Fahrenheit"""
    return data * 9 / 5 + 32


def fahrenheit_to_celsius(data):
    """A function that converts Fahrenheit to Celsius"""
    return (data - 32) * 5 / 9

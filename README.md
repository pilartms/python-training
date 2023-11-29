# Introduction to Python - BBC course

Scripts written as homework for the Introduction to Python course delivered for the BBC by Dr. John Hunt (November 2023).

## Scripts

* `analisys.py`: creates a temperature and rainfall readings data application. This is a preliminary script, which later on splits into `main.py`, `utils.py` and `readings.py` to experiment with modules.
* `main.py`: modifies the existing application so that it makes use of multiple modules, rather than being defined in a single file. It requires `utils.py` and `readings.py`.
* `readings.py`: this module holds the Reading,TemperatureReading and RainfallReading classes, as well as InvalidTemperatureException for exception handling.
* `utils.py`: this module holds utility functions such as celsius_to_fahrenheit, average, minimum etc.
* `test_utils.py`: runs a set of tests to validate the `utils.py` functions. I used pytest via PyCharm.


## Applied knowledge

* Variables, Types and Operations
* Control Flow Statements
* Data Container Types
* Functions
* Classes and Objects
* Operator Overloading
* Class Inheritance
* Modules
* Error Handling
* PyTest (via PyCharm)

# Sunint Bindra
# February 5, 2019
# timer.py
# Short Assignment 6 CS 1
# This program creates a class for a timer that acts as a stopwatch and counts down from a time until it reaches 0,
# displaying all numbers inclusive

# This imports the Counter class
from counter import *


# This creates a timer class and defines the variables hours, minutes, and seconds
class Timer:
    hours = 24
    minutes = 60
    seconds = 60


    # Sets the parameters for the class and assigns self. names for the variables, as well as creating 3 Counter objects
    def __init__(self, hours, minutes, seconds):
        self.hours = Counter(24, hours, 2)
        self.minutes = Counter(60, minutes, 2)
        self.seconds = Counter(60, seconds, 2)



    # This method returns a string with the current time in the format wanted
    def __str__(self):
        return str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)



    # This method ticks the timer down by one second and changes the display time as a real clock should by changing
    # the displayed hours, minutes, and seconds correctly
    def tick(self):
        if self.minutes.get_value() == 0 and self.seconds.get_value() == 0:
            self.hours.tick()
            self.minutes.tick()
            self.seconds.tick()
        elif self.seconds.get_value() == 0:
            self.minutes.tick()
            self.seconds.tick()
        else:
            self.seconds.tick()



    # This method returns a Boolean True if the time has reached 00:00:00, otherwise it returns False
    def is_zero(self):
        if self.hours.get_value() != 0 and self.minutes.get_value() != 0 and self.seconds.get_value() != 0:
            return False
        else:
            return True



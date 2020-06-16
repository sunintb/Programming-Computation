# Sunint Bindra
# February 5, 2019
# timer_driver.py
# Short Assignment 6 CS 1
# This program creates a stopwatch based on the classes Timer and Counter and counts dowwn from 1 hours 30 minutes to 0



# This imports the Timer class and imports the time function
from timer import *
import time


# The constructor example_timer is created for objects of the Timer class
example_timer = Timer(1, 30, 0)


# Below variables are defined to be used in calculating num_loops
hours = 1
minutes = 30
seconds = 0


# This calculates num_loops, which is used in the for loop. num_loops is the total number of #'s (+1 for 00:00:00)
# that will be counted so that a range can be defined of how many time readings the timer should display
num_loops = seconds + (minutes * 60) + (hours * 60 * 60) + 1


# This for loop below prints the starting time (in this case 01:30:00) and counts down till 00:00:00 waiting 1 second
# before displaying the time using the time.sleep function
for i in range(num_loops):
   print(example_timer)
   example_timer.tick()
   time.sleep(1)
   # do sleep counter timer
   # do sleep counter timer





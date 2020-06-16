# Sunint Bindra
# February 5, 2019
# counter.py
# Short Assignment 6 CS 1
# This program creates a class for a counter that counts down from a number and repeats once it cycles through 0,
# lowering the limit of the counter by 1 after each cycle through


# This imports the Counter class
from counter import *



# The constructor counter_a and counter_b are created for objects of the counter class
counter_a = Counter(100, 190, 1)
counter_b = Counter(50,40,3)



# This creates a loop for  counter_a. This demonstrates the tick and get_value methods, that the counter works properly
# and that the parameters, constructor, and object all work as intended. This also prints an error message as
# instructed since the initial value is higher than the limit. This also creates a new initial value based on the
# limit -1, and then prints out the numbers.
while counter_a.get_value() > 0:
    print(counter_a)
    counter_a.tick()


# This creates a loop for  counter_b. # This demonstrates aspects similar to counter_a, but also
# shows the methods of using 3 digits and leading 0's. This also shows no error message is printed when the initial
# value is less than the limit and that the counting will thus start from the initial value.
while counter_b.get_value() > 5:
    print(counter_b)
    counter_b.tick()
# Sunint Bindra
# February 5, 2019
# counter.py
# Short Assignment 6 CS 1
# This program creates a class for a counter that counts down from a number and repeats once it cycles through 0,
# lowering the limit of the counter by 1 after each cycle through



# Assigns the name counter to a class
class Counter:


    # Sets the parameters for the class and assigns self. names for the variables
    def __init__(self, limit, initial = 0, min_digits = 1):
        self.limit = limit
        self.value = initial
        self.min_digits = min_digits


        # This if statement makes sure that the limit of a number cannot be exceeded even if the initial value is
        # supposedly higher. While this is not important for a clock since there are constant max values for hours,
        # seconds, and minutes, but if we assign random values for a counter this way it makes logical sense and ensures
        # the limit actually serves its intended purpose
        if self.value >= self.limit:
            print("Error, initial value is higher than limit. New initial value has been generated equal to limit - 1.")
            self.value = self.limit - 1



    # This method returns an integer for whatever the next value in the counter is
    def get_value(self):
        return int(self.value)



    # This method adds on leading 0's based on the number assigned to min_digits
    def __str__(self):
        self.string = str(self.value)
        while len(self.string) < self.min_digits:
            self.string = "0" + self.string
        return self.string



    # This method acts as a ticker for the counter and counts down by a value of 1 and returns a false boolean
    # until the value reaches 0, at which point the new limit is the previous limit minus 1 and returns a true boolean
    def tick(self):
        if self.value > 0:
            self.value = self.value - 1
            return False
        else:
            self.value = self.limit - 1
            return True






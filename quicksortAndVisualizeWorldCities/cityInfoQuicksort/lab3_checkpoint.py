# Sunint Bindra
# February 20, 2019
# lab3_checkpoint.py
# lab3cs1
# This program is a driver for the city function that imports the city class and is able to take the location
# info from the list and `

# Imports the city class to be used in the driver
from city import *


# Opens both text files, the original one with all city information and the empty txt file we add to, respectively
in_file = open("world_cities.txt", "r")
out_file = open("cities_out.txt", "w")

# Creates a for loop in which each line is stripped to get rid of whitespace, split by commas to make sure it is
# following the English format indicated by the assignment page, and creates a city object with that information
# to be used to write a txt file with the information
for line in in_file:
    clauses = line.strip()
    new_list = clauses.split(",")
    City_object = City(new_list[0], new_list[1], new_list[2], new_list[3], new_list[4], new_list[5])
    out_file.write(str(City_object) + "\n")



# Both files are closed now
out_file.close()
in_file.close()


# Sunint Bindra
# February 22, 2019
# visualize_cities.py
# lab3cs1
# This program draws the world map and all the cities with a time gap b/w each pinpoint


# Imports the city class to be used in the driver and other stuff that is used
from cs1lib import *
from city import *
from quicksort import *


# This loads the image of the world map
img = load_image("world.png")

# Sets the count to 0 that will be used later
count = 0

# Creates an empty global list variable
global list_for_pop
list_for_pop = []


# The next 10 lines 30 lines approximately create a list of the sorted objects, as well as sorting them by
# population
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


def compare_population(City_1, City_2):
    return int(City_1.population) <= int(City_2.population)


def write_file(list, file_name):
    in_pop_file = open(file_name, "w")
    for i in list:
        in_pop_file.write(str(i) + "\n")


in_file = open("world_cities.txt", "r")
for line in in_file:
    clauses = line.strip()
    new_list = clauses.split(",")
    City_object = City(new_list[0], new_list[1], new_list[2], new_list[3], new_list[4], new_list[5])
    list_for_pop.append(City_object)

sort(list_for_pop, compare_population)


# This is the primary draw function, by drawing a red dot in the cities from the highest to decreasing population
def draw_cities():
    global count
    draw_image(img, 0, 0)

    for i in range(0, count):
         set_fill_color(1,0,0)
         height = (360 - ((float(list_for_pop[i].latitude) + 90) * 2))
         width = ((float(list_for_pop[i].longitude) + 180) * 2)
         draw_circle(width, height, 2)
    if count < 50:
        count = count + 1


# This start the graphics window and opens it and begins the program
start_graphics(draw_cities, width = 720, height = 360, framerate = 1)
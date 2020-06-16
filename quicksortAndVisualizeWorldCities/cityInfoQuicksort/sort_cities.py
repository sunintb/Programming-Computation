# Sunint Bindra
# February 20, 2019
# sort_cities.py
# lab3cs1
# This program sorts the cities list according to the different parameters such as alphabetical, by population, etc.



# Imports the city class as well as the quicksort function
from city import *
from quicksort import *



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



# All of these functions are comparisions based on different types of sorting requested
def compare_population(City_1, City_2):
    return int(City_1.population) <= int(City_2.population)

def compare_latitude(City_1, City_2):
    return float(City_2.latitude) <= float(City_1.latitude)

def compare_alpha(City_1, City_2):
    return City_2.name.upper() <= City_1.name.upper()


# This function writes the list into the txt file
def write_file(list, file_name):
    in_pop_file = open(file_name, "w")
    for i in list:
        in_pop_file.write(str(i) + "\n")


in_file = open("world_cities.txt", "r")


# Creates an empty list to be used for appending into
list_for_pop = []


# Creates a for loop in which each line is stripped to get rid of whitespace, split by commas to make sure it is
# following the English format indicated by the assignment page, and creates a city object with that information
# to be used to write a txt file with the information
for line in in_file:
    clauses = line.strip()
    new_list = clauses.split(",")
    City_object = City(new_list[0], new_list[1], new_list[2], new_list[3], new_list[4], new_list[5])
    list_for_pop.append(City_object)


# All of these lines sort the list according to the requested format and then write into the corresponding txt files
sort(list_for_pop, compare_population)

write_file(list_for_pop, "cities_population.txt")

sort(list_for_pop, compare_alpha)

write_file(list_for_pop, "cities_alpha.txt")

sort(list_for_pop, compare_latitude)

write_file(list_for_pop, "cities_latitude.txt")













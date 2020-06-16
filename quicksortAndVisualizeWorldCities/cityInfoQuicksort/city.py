# Sunint Bindra
# February 20, 2019
# city.py
# lab3cs1
# This program is a class for the city function that allows taking in information about a city/location and then
# modifying it to create a string of specific information



# Creates a class named Body
class City:



    # Defines parameters that will be used, mostly relating to different statistical and geographical information points
    # of the city/location
    def __init__(self, cc, name, region, population, latitude, longitude):
        self.country_code = cc
        self.name = name
        self.region = region
        self.population = population
        self.latitude = latitude
        self.longitude = longitude



    # This method returns a string with the selected information (name, pop, longitude, latitude)
    def __str__(self):
        self.city_info = str(self.name + str(",") + str(int(self.population)) + str(",") + str(float(self.latitude)) + str(",") + str(float(self.longitude)))
        return self.city_info





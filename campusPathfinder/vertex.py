# Sunint Bindra
# vertex.py
# This program is a vertex class that has all the methods that are used

from cs1lib import *


class Vertex:


    # Defines instance variables used
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.list = []
        self.str = ""


    # Sets the vertixes adjacent to the existing vertex
    def setting_adjacent_vertices(self, temp_list):
        self.list.append(temp_list)
        if self.str == "":
            self.str = self.str + " " +  temp_list.get_name()


    # creates the string as requested
    def __str__(self):
            adjacent_vert_str = ""
            for i in range(len(self.list) - 1):
                adjacent_vert_str = adjacent_vert_str + self.list[i].get_name() + ", "

            adjacent_vert_str = adjacent_vert_str + self.list[-1].get_name()

            vertex_info = str(self.name) + "; " + "Location:" + str(self.x) + "," + str(self.y) + "; " + "Adjacent vertices: " + str(adjacent_vert_str)

            return vertex_info


    # returns the name of the vertex
    def get_name(self):
        return self.name


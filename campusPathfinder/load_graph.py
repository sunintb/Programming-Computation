# Sunint Bindra
# vertex.py
# This program loads the graph and creates the dictionary with all the vertixes used


from vertex import *

my_dictionary = {}
def load_graph(file_name):



    # Opens the text file
    in_file = open("dartmouth_graph.txt", "r")

    # Creates a for loop in which each line is stripped to get rid of whitespace, split by commas to make sure it is
    # following the English format indicated by the assignment page, and creates a vertex object with that information
    # to be added to the dictionary
    for line in in_file:
        section = line.split(";")
        section[2].strip(" ")
        vert_section = section[0]
        section[2] = section[2].strip("\n")
        vert_x_and_y = section[2].split(",")
        vertex_line = Vertex(vert_section, vert_x_and_y[0], vert_x_and_y[1])
        my_dictionary[vert_section] = vertex_line

    in_file.close()

    # This pass over the file creates the adjacency list for all the vertexes created in the earlier for lopp
    in_file = open("dartmouth_graph.txt", "r")
    for line in in_file:
        section_2nd = line.split("; ")
        section_3rd = section_2nd[1].split(", ")


        for i in range(len(section_3rd)):
            for key in my_dictionary:
                if my_dictionary[key].get_name() == section_3rd[i]:

                    my_dictionary[section_2nd[0]].setting_adjacent_vertices(my_dictionary[key])


    in_file.close()
    return my_dictionary

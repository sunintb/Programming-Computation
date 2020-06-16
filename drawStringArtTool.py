# This program draws string art based on the values inputted for the parameters
# sa5cs1
# Sunint Bindra
# January 31, 2019


# import functions required for drawing graphics and string art
from cs1lib import *


# The function that takes in all input parameters and draws the two main sticks and all the strings in between them
def draw_string_art(xa1, ya1, xa2, ya2, xb1, yb1, xb2, yb2, n_s):

    # clears the window, sets the stroke colour to red ans stroke pixel width to 3, and draws the two main sticks
    clear()
    set_stroke_color(1,0,0)
    set_stroke_width(3)
    draw_line(xa1, ya1, xa2, ya2)
    draw_line(xb1, yb1, xb2, yb2)
    f = 0 # defines f so it can be used in the following while loop

    # This is a while loop that draws the strings and sets the stroke colour by using variable f, also sets stroke width
    while f <= 1:
     set_stroke_width(1)
     set_stroke_color(0, f, 1.0 - f)
     draw_line(xa1 + f * (xa2 - xa1), ya1 + f * (ya2 - ya1), xb2 - f * (xb2 - xb1), yb2 - f * (yb2 - yb1))
     f = f + (1 / (n_s - 1))



# A seperate function without parameters so it can be inputted into the start_graphics function
def draw_main():
    set_clear_color(0, 0, 0)
    draw_string_art(80, 80, 70, 250, 280, 50, 220, 200, 30)



# Opens the graphics window and draws the string art
start_graphics(draw_main)

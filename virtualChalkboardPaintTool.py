# This program acts as a basic paint software that draws when mouse is clicked and stops drawing when released. It also
# allows you to change the pen colour by pressing keys that correspond to various colours.
# Program Name: sa4cs1
# Author: Sunint Bindra
# January 16, 2019
# Computer Science 1


# This imports all the functions we will need
from cs1lib import *


# Here we assign global variables and define them
global x
global y
x = 0
y = 0
global old_x
global old_y


# This sets the mouse_pressed function to false initially, since the mouse has not yet been clicked
global mouse_pressed
mouse_pressed = False


# This function defines what happens when the mouse is clicked
def mouse_press(mx, my):
    global mouse_pressed, x, y
    mouse_pressed = True
    x = mx
    y = my


# This function defines what happens when the mouse is released
def mouse_release(mx, my):
    global mouse_pressed, x, y
    mouse_pressed = False
    x = mx
    y = my


# This function defines what happens when the mouse is moved
def mouse_move(mx, my):
    global x, y
    x = mx
    y = my
    if mouse_pressed:
        draw_line(old_x, old_y, x, y)


# This is the main draw function that sets the graphics window with a black background and an initial white
# stroke colour. It also changes the x and y coordinates from the old to new ones everytime their is a line drawn
global frame
frame = 1
def draw_main():
    global old_x, old_y, x, y, frame
    set_clear_color(0, 0, 0)
    if(frame ==1):
        clear()
        set_stroke_color(1,1,1)
    old_x = x
    old_y = y
    set_stroke_width(2)
    frame += 1


# This defines all the key presses and their respective colour for the pen stroke colour
def key_press(k):
    # This sets the stroke colour to red when the r key is pressed
    if k == ("r"):
        set_stroke_color(1, 0, 0)
    # This sets the stroke colour to blue when the b key is pressed
    if k == ("b"):
       set_stroke_color(0, 0, 1)
    # This sets the stroke colour to green when the g key is pressed
    if k == ("g"):
        set_stroke_color(0, 1, 0)
    # This sets the stroke colour to yellow when the y key is pressed
    if k == ("y"):
        set_stroke_color(.5, .5, 0)
    # This sets the stroke colour to white when the w key is pressed
    if k == ("w"):
        set_stroke_color(1, 1, 1)


# This starts the graphics window
start_graphics(draw_main, mouse_press=mouse_press, mouse_release=mouse_release, mouse_move=mouse_move, key_press=key_press)

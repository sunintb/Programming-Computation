# This program is an arcade ping pong game
# Program Name: lab1cs1
# Author: Sunint Bindra
# January 19, 2019
# Computer Science 1


# Importing all functions that will be required for this program
from cs1lib import *


# Labelling and defining variables
global x_l
global y_l
global x_r
global y_r
game_playing = False

x_l = 0
y_l = 0
x_r = 380
y_r = 320
width = 20
height = 80

radius = 10
WINDOW_CENTER = 200
x_center = 200
y_center = 200
x_velocity = 2
y_velocity = 2

pressed_a = False
pressed_z = False
pressed_k = False
pressed_m = False
pressed_space = False


# Function for drawing the background
def draw_background():
    set_clear_color(1, 0, 0)
    clear()


# set what happens when a key is pressed (to register as true)
def ifkey_press(key):
    global pressed_a, pressed_z, pressed_k, pressed_m, pressed_space
    if key == "a":
        pressed_a = True
    if key == "z":
        pressed_z = True
    if key == "k":
        pressed_k = True
    if key == "m":
        pressed_m = True

    # For starting new game
    if key == " ":
        pressed_space = True

    # For ending program with q key
    if key == "q":
        cs1_quit()


# set what happens when a key is released (to register as false)
def keyup(key):
    global pressed_a, pressed_z, pressed_k, pressed_m
    if key == "a":
        pressed_a = False
    if key == "z":
        pressed_z = False
    if key == "k":
        pressed_k = False
    if key == "m":
        pressed_m = False


def draw_window():

    global x_l, y_l, x_r, y_r

    # Draws the red background
    draw_background()

    # Draws the paddles
    set_fill_color(0, 0, 0)
    draw_rectangle(x_l, y_l, width, height)
    draw_rectangle(x_r, y_r, width, height)

    # Draws the ball
    animate_circle()

    # Sets the direction of paddle movement to vertical; the 2nd condition sets the wall
    # parameters and stops the paddles from moving once they hit a wall
    if pressed_a and y_l > (0):
        y_l -= SPEED
    if pressed_z and y_l < (320):
        y_l += SPEED
    if pressed_k and y_r > (0):
        y_r -= SPEED
    if pressed_m and y_r < (320):
        y_r += SPEED


def hits_right():
    if (x_center + radius) >= 400:
        return True

def hits_left():
    if (x_center - radius) <= 0:
        return True

def hits_top():
    if y_center <= 10:
        return True

def hits_bottom():
    if y_center >= 390:
        return True

def animate_circle():
    global radius, x_center, y_center, x_velocity, y_velocity
    set_fill_color(0,0,0)
    draw_circle(x_center, y_center, radius)

    if pressed_space == True:
        x_center += x_velocity
        y_center += y_velocity


    if game_playing == False and x_velocity == 0 and y_velocity == 0:
            x_center = WINDOW_CENTER
            y_center = WINDOW_CENTER
            x_velocity = 2
            y_velocity = 2

    if hits_right():
        x_velocity = 0
        y_velocity = 0
        draw_text("Player 1 (left paddle) wins the game!", 90, WINDOW_CENTER)
        draw_text("Press spacebar to start new game", 93, WINDOW_CENTER + 15)
        game_playing == False


    if hits_left():
        x_velocity = 0
        y_velocity = 0
        draw_text("Player 2 (right paddle) wins the game!", 90, WINDOW_CENTER)
        draw_text("Press spacebar to start new game", 93, WINDOW_CENTER + 15)
        game_playing == False


    if hits_top():
        y_velocity = y_velocity * -1
    if hits_bottom():
        y_velocity = y_velocity * -1

    if (x_center + radius) == x_r and (y_center + radius) < (y_r + height) and (y_center - radius) > y_r:
        x_velocity = x_velocity * -1

    if (x_center - radius) == (x_l + width) and (y_center + radius) < (y_l + height) and (y_center - radius) > y_l:
        x_velocity = x_velocity * -1


    if pressed_space == False:
        draw_text("Press spacebar to start the game", 90, 250)











# sets the speed
SPEED = 3

# Starts graphics window of arcade pong
start_graphics(draw_window, key_press=ifkey_press, key_release=keyup)
# Sunint Bindra
# February 10, 2019
# body.py
# lab2cs1
# This program is a class for the body function that allows calculating the physics of the planet/moon as well as its
# updated position and velocity. It also draws the body.



# Imports functions that will be used to draw the bodies
from cs1lib import *


# Creates a class named Body
class Body:



    # Defines parameters that will be used, mostly relating to aspects of the bodies such as their position, velocity,
    # pixel size on screen, and colour/visual output
    def __init__(self, mass, x, y, vx, vy, mercury):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mercury = load_image(mercury.png)
        mercury = load_image("mercury.png")



    # Updates position of the bodies by adding the current position to the velocity multipled by timestep,
    # which represents the time between drawing every individual frame
    def update_position(self, timestep):
        self.x = self.x + self.vx * timestep
        self.y = self.y + self.vy * timestep



    # Updates velocity of the bodies by adding the current velocity to the acceleration multipled by timestep,
    # which represents the time between drawing every individual frame
    def update_velocity(self, ax, ay, timestep):
        self.vx = self.vx + ax * timestep
        self.vy = self.vy + ay * timestep



    # Draws the circle-shaped body using the assigned colours as well as converting the actual size to a
    # pixel size that can be seen on the screen and that the numbers fit the dimensions of python graphics window
    def draw(self, cx, cy, pixels_per_meter):
        set_fill_color(self.r, self.g, self.b)
        draw_circle(cx + pixels_per_meter * self.x, cy + pixels_per_meter * self.y, self.pixel_radius)

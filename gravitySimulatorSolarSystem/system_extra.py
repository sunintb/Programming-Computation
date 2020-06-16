## Sunint Bindra
# February 10, 2019
# body.py
# lab2cs1
# This program is a class named system that allows creating a system for the interaction of all the bodies,
# as well as making it easier to manipulate the bodies by creating methods to integrate the drawing and updating
# the bodies


# Imports math so sqrt can be used in the compute acceleration method
from math import *


# Creates a class named System
class System:



    # Defines the instance variable of the list of bodies that are objects and are used
    def __init__(self, body_list):
        self.body_list = body_list



    # Updates the position and velocity by taking in the computed acceleration. Tells the method to update the position
    #  and velocity after the time between each frame and to use the listed acceleration in the calculations
    def update(self, timestep):
        for i in range(0, len(self.body_list)):
            self.body_list[i].update_position(timestep)
            (total_ax, total_ay) = self.compute_acceleration(i)
            self.body_list[i].update_velocity(total_ax, total_ay, timestep)



    # Draws all body objects according to their parameters
    def draw(self, cx, cy, pixels_per_meter):
        for i in range(0, len(self.body_list)):
            self.body_list[i].draw(cx, cy, pixels_per_meter)



    # Computes the acceleration by looping through the list, calculating the new ax and ay values based on many
    # calculations as described in the lab assignment page, then returns those values to be used in updating position
    # and velocity
    def compute_acceleration(self, n):
        total_ax = 0
        total_ay = 0
        for i in range(0, len(self.body_list)):
            if i!=n:
                g = 6.67384e-11
                m = self.body_list[i].mass
                dx = float(self.body_list[i].x - self.body_list[n].x)
                dy = float(self.body_list[i].y - self.body_list[n].y)
                r = float(sqrt(dx*dx + dy*dy))
                a = float((g * m)/(r*r))
                ax = a * dx/r
                ay = a * dy/r
                total_ax = total_ax + ax
                total_ay = total_ay + ay
        return total_ax, total_ay



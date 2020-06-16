## Sunint Bindra
# February 15, 2019
# solar.py
# lab2cs1
# This program is a driver that creates a solar system with various bodies such as the sun, earth, venus, merucy, and
# mars. Most of is it the same as the earthmoon. py file, however the TIME_SCALE and PPM have been changed, as well as
# adding in AU and EM for

from cs1lib import *
from system import System
from body import Body

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 2000000
PIXELS_PER_METER = 8 / 1e10  # distance scale for the simulation

FRAMERATE = 30              # frames per second
TIMESTEP = 1.0 / FRAMERATE  # time between drawing each frame

# 1 Astronomical Unit
AU = 149597870700

# Mass of the Earth
EM = 5.9736e24

# The main draw function
def main():

    set_clear_color(0, 0, 0)    # black background

    clear()

    # Draw the system in its current state.
    solar.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    solar.update(TIMESTEP * TIME_SCALE)
    draw_image(mercury, -.3871 * AU, 0)


# The various objects from the system class that represent all the bodies to be displayed in the graphics window
#sun = Body(1.98892e30, 0, 0, 0, 0, 15, 1, 1, 0)
mercury = Body(.06 * EM, -.3871 * AU, 0, 0, 47890, 3, 1, .4, 0)
#venus = Body(.82 * EM, -.7233 * AU, 0, 0, 35040, 6, 0, .6, .2)
#earth = Body(1.0 * EM, -1.0 * AU, 0, 0, 29790, 7, 0, .4, 1)
#mars = Body(.11 * EM, -1.524 * AU, 0, 0, 24140, 4, .8, .2, 0)
solar = System([mercury])

start_graphics(main, 2400, framerate=FRAMERATE)
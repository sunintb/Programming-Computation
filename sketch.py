# This is a graphic drawing of a face of mickey mouse. I hope you like it!
# Program Name: SA2CS1
# Author: Sunint Bindra
# January 10, 2019
# Computer Science 1

from cs1lib import start_graphics, clear, set_fill_color, set_stroke_color, draw_circle, draw_ellipse, draw_text, draw_line, draw_rectangle, disable_stroke, enable_stroke, set_clear_color

def draw_background():
    # draw a red background
    set_clear_color(1, 0, 0)
    clear()

def draw_mickeymouse():
    draw_background()

    # draw outline of mickey's face
    set_fill_color(1, 1, 1) # set colour to white
    draw_circle(200, 200, 100)

    # draw mickey's ears
    set_fill_color(0, 0, 0) # set colour to black
    draw_circle(87, 87, 60)
    draw_circle(313, 87, 60)

    # draw mickey's eyes
    set_fill_color(1, 1, 1) # set colour to white
    draw_ellipse(225, 160, 20, 30)
    draw_ellipse(175, 160, 20, 30)
    set_fill_color(0, 0, 0) # set colour to black
    draw_ellipse(220, 173, 10, 15)
    draw_ellipse(180, 173, 10, 15)

    # draw mickey's mouth
    set_fill_color(1, 1, 1) # set colour to white
    draw_ellipse(200, 250, 60, 40)
    disable_stroke()
    draw_rectangle(120, 200, 150, 60)
    enable_stroke()
    set_stroke_color(0, 0, 0) # set colour to black
    draw_line(250, 255, 265, 265)
    draw_line(130, 265, 150, 255)

    # draw mickey's nose
    set_fill_color(0, 0, 0) # set colour to black
    draw_ellipse(200, 230, 25, 15)

    # writing my name
    draw_text("Sunint Bindra", 10, 380)

start_graphics(draw_mickeymouse)
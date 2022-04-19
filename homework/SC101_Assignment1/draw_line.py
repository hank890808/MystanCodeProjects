"""
File: draw_line.py
Name: Hank 蕭承瀚
-------------------------
This file helps the user draw lines by clicking twice.
"""

from campy.graphics.gobjects import GOval, GLine, GRect, GLabel
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

window = GWindow()

# This counts how many times the user clicked
n_click = 0
# This controls the circle which is the start of the line
SIZE = 10
first = GOval(SIZE, SIZE)

clear_button = GRect(60, 30, x=5, y=5)
clear_button_label = GLabel("Clear", x=12, y=30)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    The clear button will help the user clear the canvas.
    """
    onmouseclicked(draw_line)
    clear_button.filled = True
    clear_button.fill_color = "grey"
    window.add(clear_button)
    clear_button_label.font = "Courier-13"
    window.add(clear_button_label)


def draw_line(mouse):
    global n_click
    n_click += 1
    wanna_clear = window.get_object_at(mouse.x, mouse.y)
    if wanna_clear is clear_button or wanna_clear is clear_button_label:
        window.clear()
        n_click = 0
        window.add(clear_button)
        window.add(clear_button_label)
    elif n_click % 2 != 0:
        window.add(first, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)
    else:
        second = GLine(first.x+SIZE/2, first.y+SIZE/2, mouse.x, mouse.y)
        window.remove(first)
        window.add(second)


if __name__ == "__main__":
    main()

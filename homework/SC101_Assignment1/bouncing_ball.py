"""
File: bouncing_ball.py
Name: Hank 蕭承瀚
-------------------------
This file simulates the bouncing ball.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')

# This controls the size of the ball
ball = GOval(SIZE, SIZE)
# This counts how many times the ball bounces
n = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(bounce)
    ball.filled = True
    ball.fill_color = "black"
    ball.color = "black"
    window.add(ball, x=START_X, y=START_Y)


def bounce(mouse):
    global n
    if n >= 3 or ball.x != START_X:
        return
    else:
        n += 1
        vy = 0
        while True:
            ball.move(VX, vy)
            vy += GRAVITY
            if ball.y > window.height:
                vy = -vy*REDUCE
            track(ball.x+SIZE/2, ball.y+SIZE/2)
            pause(DELAY)
            if ball.x > window.width:
                window.clear()
                window.add(ball, x=START_X, y=START_Y)
                break


def track(x, y):
    """
    The dots represent the track of the ball.
    :param x: the x position of the ball
    :param y: the y position of the ball
    """
    dot = GOval(5, 5)
    dot.filled = True
    dot.fill_color = "black"
    window.add(dot, x=x-5/2, y=y-5/2)


if __name__ == "__main__":
    main()

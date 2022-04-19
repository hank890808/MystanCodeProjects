"""
File: bouncing_ball.py
Name: Hank 蕭承瀚
-------------------------
This file simulates the bouncing ball.
"""

from campy.graphics.gobjects import GOval, GLine, GRect, GLabel
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked, onmousedragged, onmousereleased

DELAY = 30
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
V_RATIO = 0.1


window = GWindow(800, 500, title='bouncing_ball.py')

# This controls the size of the ball
ball = GOval(SIZE, SIZE)
# The initial position of the ball
init_x = 0
init_y = 0
# The initial velocity of the ball
vx = 0
vy = 0


def main():
    """
    This program will simulate a ball bouncing in the canvas,
    while the initial position and the velocity are decided by
    the user clicking and dragging the mouse.
    """
    onmouseclicked(start)
    onmousedragged(ready_for_bounce)
    onmousereleased(bounce)


def start(mouse):
    """
    As the user presses the mouse, it will record
    the position as the starting point.
    """
    global init_x, init_y
    init_x = mouse.x
    init_y = mouse.y
    ball.filled = True
    ball.fill_color = "black"
    window.add(ball, x=init_x-SIZE/2, y=init_y-SIZE/2)


def ready_for_bounce(mouse):
    """
    As the user drags the mouse, he/she can control
    the velocity and direction of the ball.
    """
    global vx, vy
    window.clear()
    window.add(ball, x=init_x-SIZE/2, y=init_y-SIZE/2)
    arrow_line = GLine(init_x, init_y, mouse.x, mouse.y)
    window.add(arrow_line)
    if mouse.x < init_x and mouse.y < init_y:
        arrow1 = GLine(mouse.x, mouse.y, mouse.x + 20, mouse.y)
        arrow2 = GLine(mouse.x, mouse.y, mouse.x, mouse.y + 20)
    elif mouse.x > init_x and mouse.y < init_y:
        arrow1 = GLine(mouse.x, mouse.y, mouse.x - 20, mouse.y)
        arrow2 = GLine(mouse.x, mouse.y, mouse.x, mouse.y + 20)
    elif mouse.x > init_x and mouse.y > init_y:
        arrow1 = GLine(mouse.x, mouse.y, mouse.x - 20, mouse.y)
        arrow2 = GLine(mouse.x, mouse.y, mouse.x, mouse.y - 20)
    else:
        arrow1 = GLine(mouse.x, mouse.y, mouse.x + 20, mouse.y)
        arrow2 = GLine(mouse.x, mouse.y, mouse.x, mouse.y - 20)
    window.add(arrow1)
    window.add(arrow2)
    vx = (mouse.x - init_x)*V_RATIO
    vy = (mouse.y - init_y)*V_RATIO


def bounce(mouse):
    """
    As the user releases the mouse, the ball starts bouncing.
    """
    global vx, vy
    window.clear()
    window.add(ball)
    while True:
        ball.move(vx, vy)
        pause(DELAY)
        if ball.x <= 0 or ball.x >= window.width:
            vx = -vx*REDUCE
        vy += GRAVITY
        if ball.y <= 0 or ball.y >= window.height:
            vy = -vy*REDUCE


if __name__ == "__main__":
    main()

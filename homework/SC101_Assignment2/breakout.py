"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

# CONSTANTS
FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    graphics = BreakoutGraphics()
    break_brick = 0

    # Animation loop
    for i in range(NUM_LIVES):
        dx = graphics.get_dx()
        dy = graphics.get_dy()
        while True:
            if graphics.start:
                dx = graphics.get_dx()
                dy = graphics.get_dy()
            graphics.ball.move(dx, dy)
            graphics.start = False

            # Hit the wall
            if graphics.ball.x < 0 or graphics.ball.x > graphics.window.width - graphics.ball.width:
                dx *= -1
            if graphics.ball.y < 0:
                dy *= -1

            # Hit the paddle and the bricks
            maybe_object = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
            if maybe_object is not None:
                if maybe_object is graphics.paddle:
                    dy *= -1
                else:
                    dy *= -1
                    graphics.window.remove(maybe_object)
                    break_brick += 1
            else:
                maybe_object = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y)
                if maybe_object is not None:
                    if maybe_object is graphics.paddle:
                        dy *= -1
                    else:
                        dy *= -1
                        graphics.window.remove(maybe_object)
                        break_brick += 1
                else:
                    maybe_object = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)
                    if maybe_object is not None:
                        if maybe_object is graphics.paddle:
                            dy *= -1
                        else:
                            dy *= -1
                            graphics.window.remove(maybe_object)
                            break_brick += 1
                    else:
                        maybe_object = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                                     graphics.ball.y + graphics.ball.height)
                        if maybe_object is not None:
                            if maybe_object is graphics.paddle:
                                dy *= -1
                            else:
                                dy *= -1
                                graphics.window.remove(maybe_object)
                                break_brick += 1

            # Lose life
            if graphics.ball.y > graphics.window.height - graphics.ball.height:
                graphics.ball_restart()
                break

            # Win
            if break_brick == graphics.n_brick:
                graphics.win()
                break

            pause(FRAME_RATE)


if __name__ == '__main__':
    main()

"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

# CONSTANTS
BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 5    # Initial vertical speed for the ball
MAX_X_SPEED = 4        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2, y=window_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(2*ball_radius, 2*ball_radius, x=window_width/2-ball_radius, y=window_height/2-ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.ball_start)
        onmousemoved(self.paddle_move)
        self.start = False

        # Draw bricks
        self.cols = brick_cols
        self.rows = brick_rows
        for i in range(self.cols):
            for j in range(self.rows):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.window.add(self.brick, x=(brick_width+brick_spacing)*i,
                                y=(brick_height+brick_spacing)*j + brick_offset)
        self.n_brick = brick_cols * brick_rows

        # Score
        self.score = 0
        self.score_text = GLabel(self.score)
        self.score_text.font = "-30"
        # self.window.add(self.score_text, x=window_width-self.score_text.width, y=window_height)

    def ball_start(self, mouse):
        if self.__dx == 0 and self.__dy == 0:
            self.start = True
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx
            self.__dy = INITIAL_Y_SPEED

    def paddle_move(self, mouse):
        if self.paddle.width/2 <= mouse.x <= self.window.width - self.paddle.width/2:
            paddle_x = mouse.x - self.paddle.width/2
        elif mouse.x < self.paddle.width/2:
            paddle_x = 0
        else:
            paddle_x = self.window.width-self.paddle.width
        self.window.add(self.paddle, x=paddle_x, y=self.paddle.y)

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def ball_restart(self):
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)
        self.__dx = 0
        self.__dy = 0

    def win(self):
        self.window.clear()
        win_text = GLabel("YOU WIN!")
        win_text.font = "-40"
        self.window.add(win_text, x=(self.window.width-win_text.width)/2, y=(self.window.height+win_text.height)/2)

    def score(self, break_brick):
        self.score = 100 * break_brick
        self.score_text = self.score

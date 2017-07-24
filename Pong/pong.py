# Pong game in micropython
# based upon:
#   1. http://python-alhindi.blogspot.nl/2013/11/game-pong.html
#   2. http://educ8s.tv/arduino-pong-game/
# 2017_0101 PePo in progress
# TODO: score, user-controlled paddle

from machine import Pin, I2C
import ssd1306
import gfx
from time import sleep

# initialize globals
WIDTH = 64
HEIGHT = 48       

# I2C, oled dependencies
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
#i2c.scan()   #[60]
oled = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)
#oled.fill(0) # blank oled
#oled.show()
graphics = gfx.GFX(WIDTH,HEIGHT,oled.pixel)

# Base object class
class Thing:

    # Initializes the object with coordinates, size and color
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vx = 0
        self.vy = 0
        self.color = color

    # Updates object by moving it and checking if it's in screen range
    def update(self, screenWidth, screenHeight):
        self.x += self.vx
        self.y += self.vy

        if self.x < 0: self.x = 0
        if self.y < 0: self.y = 0
        if self.x > screenWidth - self.w: self.x = screenWidth - self.w
        if self.y > screenHeight - self.h: self.y = screenHeight - self.h

    # Must be implemented by child classes
    def draw(self):
        pass

    # Returns whether object collides with another object (rectangular collision detection)
    def collides(self, obj):
        return self.y < obj.y + obj.h and self.y + self.h > obj.y and self.x < obj.x + obj.w and self.x + self.w > obj.x

    # Called when object collides with anoher object, must be implemented by child classes
    def onCollide(self, obj):
        pass

# Paddle class
class Paddle(Thing):
    # Paddle properties
    width = 5 #PADDLE_WIDTH = 2
    color = 1 #PADDLE_COLOR = 1 #(1, 1, 1)   OLED is B/W
    height = 20 #PADDLE_HEIGHT = 20
    speed = 1 #PADDLE_SPEED = 1
    # Initializes Paddle object
    def __init__(self, x, y):
        super(Paddle, self).__init__(x, y, self.width, self.height, self.color)
        #super(Paddle, self).__init__(x, y, PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_COLOR)

    # Draws paddle with a rectangle
    def draw(self):
        graphics.fill_rect(self.x, self.y, self.w, self.h, self.color)
        #oled.show()

    # Moves paddle up
    def moveUp(self):
        self.vy -= self.speed #PADDLE_SPEED

    # Moves paddle down
    def moveDown(self):
        self.vy += self.speed #PADDLE_SPEED

    # Stops moving the paddle
    def stopMoving(self):
        self.vy = 0


# ComputerPaddle class
class ComputerPaddle(Paddle):

    # Initializes ComputerPaddle object
    def __init__(self, x, y):
        super(ComputerPaddle, self).__init__(x, y)

    # Adjust Y-velocity based on speed and direction of ball
    def update(self, ball, screenWidth, screenHeight):
        super(ComputerPaddle, self).update(screenWidth, screenHeight)

        if ball.vx < 0: 
            self.stopMoving()
            return

        ballX = ball.x
        ballY = ball.y
        ballVX = ball.vx
        ballVY = ball.vy

        while ballX + ball.w < self.x:
            ballX += ballVX
            ballY += ballVY
            if ballY < 0 or ballY > screenHeight - ball.h: ballVY = -ballVY

        if ballY > self.y + self.h: self.moveDown()
        elif ballY + ball.h < self.y: self.moveUp()
        else: self.stopMoving()


# Ball class
class Ball(Thing):
    # Ball properties
    #BALL_RADIUS = 2
    #BALL_COLOR = 1 #(1, 1, 1)   OLED is B/W
    #BALL_INITIAL_VX = -5
    #BALL_INITIAL_VY = -5
    radius = 2 #BALL_RADIUS
    color = 1 #BALL_COLOR, OLED is B/W
    # Initializes the Ball object along with initial velocities
    def __init__(self, x, y):
        super(Ball, self).__init__(x, y, self.radius, self.radius, self.color)
        #super(Ball, self).__init__(x, y, BALL_RADIUS, BALL_RADIUS, BALL_COLOR)
        self.startX = x
        self.startY = y
        self.vx = -5 #BALL_INITIAL_VX
        self.vy = -5 #BALL_INITIAL_VY

    # Updates the ball object, if it hits screen edge then negate velocity
    def update(self, screenWidth, screenHeight):
        super(Ball, self).update(screenWidth, screenHeight)

        if self.x == 0 or self.x == screenWidth - self.w: self.vx = -self.vx
        if self.y == 0 or self.y == screenHeight - self.h: self.vy = -self.vy

    # Resets the ball back to its initial coordinates
    def reset(self):
        self.x = self.startX
        self.y = self.startY
        self.vx = -5 #BALL_INITIAL_VX
        self.vy = -5 #BALL_INITIAL_VY

    # Draws a circle onto screen to represent the ball
    ##2017_01010 PePo
    def draw(self):
        graphics.fill_circle(self.x, self.y, self.w, self.color) 
        #oled.show() # slows down movement

    # If ball collides with another object, then negate both velocities by a random amount
    def onCollide(self, obj): 

        # If ball is "inside" of paddle, then reposition it so it's just outside the paddle
        if self.x < obj.x + obj.w: self.x = obj.x + obj.w
        elif self.x + self.w > obj.x: self.x = obj.x - self.w
        if self.y < obj.y + obj.h: self.y = obj.y + obj.h
        elif self.y + self.h > obj.y: self.y = obj.y - self.h

        #PePo: needed a random generator!
        rx = -2 #int(random.uniform(-3, 5))
        ry = 2  #int(random.uniform(-2, 4))

        self.vx = -self.vx + rx
        self.vy = -self.vy + ry

def drawCourt():
    graphics.rect(0,0, WIDTH-1,HEIGHT-1, 1)
    oled.show()
    
def setup():
    oled.fill(0) # clear screen
    oled.text("Pong", 10, 0) # splashscreen
    oled.text("game", 10, 20)
    oled.show()
    sleep(2)
    
    oled.fill(0) ## clear screen
    drawCourt() # draw game board

def gameLoop():
    left=0
    while True:
        # clear current display
        oled.fill(0)

        # update ball
        ball.update(WIDTH, HEIGHT)

        #userPaddle movement TODO: user controlled!
        #update userPaddle
        left = left + 1
        if left < 10: 
            userPaddle.moveDown()
        elif left > 20:
            left = 0
        elif left > 10:
            userPaddle.moveUp()
        #else: 
        #    userPaddle.stopMoving()
        userPaddle.update(WIDTH, HEIGHT)

        # update computerPaddle
        computerPaddle.update(ball, WIDTH, HEIGHT)

        # check for ball collisions
        if ball.collides(userPaddle):
            print("ball hits user paddle")
            userPaddle.onCollide(ball)
        if ball.collides(computerPaddle):
            print("ball hits computer paddle")
            computerPaddle.onCollide(ball)

        #draw updated game state
        ball.draw()
        userPaddle.draw()
        computerPaddle.draw()
        drawCourt() # draw game board

# start game
#instance a ball
ball = Ball(32, 22)
userPaddle = Paddle(1,20)
computerPaddle = ComputerPaddle(59, 24)

setup()
gameLoop()

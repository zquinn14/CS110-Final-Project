import pygame
import math
import random

""""COLORS"""
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREENISH = (0, 50, 50)
BLUEISH = (0, 255, 204)
GREY = (100, 100, 150)


class Paddle(pygame.sprite.Sprite):
    state = 0

    def __init__(self):
        super().__init__()
        self.paddleY = 440
        self.paddleLeft = 310
        self.paddleWidth = 100
        self.paddleHeight = 10

        self.paddle_x_change = 0
        self.key_press = 0

        self.screenWidth = 640
        self.screenHeight = 480

        self.image = pygame.Surface([self.paddleWidth, self.paddleHeight])
        self.rect = self.image.get_rect()
        self.rect.x = (self.screenWidth - self.paddleWidth) / 2
        self.rect.y = 440
        self.image.fill(GREY)

    def movePaddle(self, key_press):
        """x = 1 is the left arrow
        x = 2 is the right arrow
        x = 3 is the spacebar"""
        if key_press == 0:
            self.paddle_x_change = 0
        if key_press == 1:
            self.paddle_x_change = -8
        elif (key_press == 2):
            self.paddle_x_change = 8

class Ball(pygame.sprite.Sprite):
    xcomp = 320
    ycomp = 432
    ballRadius = 8
    def __init__(self, speed = 8):
        super().__init__()
        self.p = Paddle()
        self.speed = speed

        self.angle = random.randrange(-45, 45)

        self.screenWidth = 640

        self.image = pygame.Surface([self.ballRadius, self.ballRadius])
        self.rect = self.image.get_rect()
        self.image.fill(BLUEISH)
        self.rect.x = 315
        self.rect.y = 430

    def rebound(self, value):
        """REBOUNDS OR BOUNCES BALL OF OF WALL"""
        self.angle = (180 - self.angle) % 360
        self.angle -= value

    def update(self, state=0):
        if state == 1:
            """BALL LOCATION UPDATE"""
            # CONVERTS DIRECTION ANGLE TO RADIANS
            directionRad = math.radians(self.angle)

            """ANGLE RADIAN CONVERSION TO SIN AND COS"""
            self.xcomp += self.speed * math.sin(directionRad)
            self.ycomp -= self.speed * math.cos(directionRad)

            """CHANGES X AND Y OF BALL COORDINATE"""
            self.rect.x = self.xcomp
            self.rect.y = self.ycomp

            """IF STATEMENTS FOR BALL REBOUND"""
            if self.ycomp <= 0:
                self.rebound(0)
                self.ycomp = 1
            if self.xcomp <= 0:
                self.angle = (360 - self.angle) % 360
                self.xcomp = 1
            if self.xcomp > (self.screenWidth - self.ballRadius):
                self.angle = (360 - self.angle) % 360
                self.xcomp = (self.screenWidth - self.ballRadius) - 1
            if self.ycomp > 480:
                return True
            else:
                return False

class Brick(pygame.sprite.Sprite):
    """CLASS FOR THE CREATION OF BLOCKS"""
    #Class variable
    width = 48
    height = 10

    def __init__(self, color, xcor, ycor):
        super().__init__()
        """INITIALIZES BLOCK COLOR AND COORDINATES"""
        self.image = pygame.Surface([Brick.width, Brick.height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = xcor
        self.rect.y = ycor
        
    @classmethod
    def build_bricks(cls, bricks, brk_num, brk_top, allSprites):
        for i in range(5):
            rand_color = (255 * random.random(), 255 * random.random(), 255 * random.random())
            acolor = rand_color
            for j in range(1, brk_num):
                brick = cls(acolor, j * (cls.width + 2) + 1, brk_top)
                bricks.add(brick)
                allSprites.add(brick)
            brk_top += cls.height + 2

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.wallWidth = width
        self.wallHeight = height
        self.image = pygame.Surface([self.wallWidth, self.wallHeight])
        self.rect = self.image.get_rect()
        self.image.fill(GREENISH)
        self.rect.x = x
        self.rect.y = y

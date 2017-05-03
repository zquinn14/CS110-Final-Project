import pygame
import math
import random
import sys

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
        elif key_press == 1 and self.rect.x <= 0:
            self.rect.x = 0

        elif (key_press == 2):
            self.paddle_x_change = 8
        elif key_press == 2 and self.rect.x >= 480:
            self.rect.x = 480

class Ball(pygame.sprite.Sprite):
    angle = random.randrange(-45,45)
    speed = 8
    xcomp = 320
    ycomp = 432
    ballRadius = 8
    def __init__(self):
        super().__init__()
        self.p = Paddle()

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
            #self.xcomp = self.rect.x
            #self.ycomp = self.rect.y

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

class Controller(pygame.sprite.Sprite):

    """Class Variables:"""

    #Screen Dimensions
    displayDimensions = (640,480)

    #Brick Number and height from top
    topBrick = 80
    bricksNum = 12

    def __init__(self):
        super().__init__()

        """PYGAME INITIALIZATION"""
        pygame.init()

        """Setup of window or screen"""
        self.gameDisplay = pygame.display.set_mode(self.displayDimensions)
        pygame.display.set_caption('Brick Ball!')

        """SPRITE GROUPS"""
        self.bricks = pygame.sprite.Group()
        self.ballGroup = pygame.sprite.Group()
        self.allSprites = pygame.sprite.Group()

        """PADDLE"""
        self.p = Paddle()
        self.allSprites.add(self.p)

        """BALL"""
        self.b = Ball()
        self.allSprites.add(self.b)
        self.ballGroup.add(self.b)

        """BRICK CREATION - calls class variables"""
        Brick.build_bricks(self.bricks, self.bricksNum, self.topBrick, self.allSprites)

        """Initialize state value"""
        self.state = 0

    def game(self):
        clock = pygame.time.Clock()
        typicalFont = pygame.font.SysFont('Helvetica', 50, bold=True)
        gameExit = False
        key_press = 0

        """GAME LOOP"""
        while True:

            clock.tick(60)
            self.gameDisplay.fill(GREENISH)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            """COLLISION HANDLING"""
            if pygame.sprite.spritecollide(self.p, self.ballGroup, False):
                control = (self.p.rect.x + self.p.paddleWidth / 2) - (self.b.rect.x + self.b.ballRadius / 2)
                self.b.rect.y = 432
                self.b.rebound(control)

                """Helps make ball bounce smoothly off paddle"""
                if not gameExit:
                    gameExit = self.b.update(self.state)

            if len(self.bricks) != 0 and self.b.rect.y > 440:
                msg = typicalFont.render("LOST", 1, WHITE)
                msgpos = msg.get_rect(centerx = 320)
                msgpos.bottom = 230
                self.gameDisplay.blit(msg, msgpos)

            hitBlocks = pygame.sprite.spritecollide(self.b, self.bricks, True)
            if len(hitBlocks) > 0:
                self.b.rebound(0)
            if len(self.bricks) == 0:
                winmsg = typicalFont.render('Winner Winner Chicken Dinner', 0, WHITE)
                winmsgpos = winmsg.get_rect(centerx = 320)
                winmsgpos.bottom = 230
                self.gameDisplay.blit(winmsg, winmsgpos)

            """PADDLE CONTROL"""
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    key_press = 0
                    self.p.movePaddle(key_press)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and self.state == 1:
                key_press = 1
                self.p.movePaddle(key_press)

            elif keys[pygame.K_RIGHT] and self.state == 1:
                key_press = 2
                self.p.movePaddle(key_press)

            elif keys[pygame.K_SPACE] and self.state == 0:
                self.state = 1

            self.allSprites.draw(self.gameDisplay)

            self.p.rect.x += (self.p.paddle_x_change)

            self.b.update(self.state)

            pygame.display.update()

        pygame.quit
        quit()

    # @classmethod
    # def getHiScor(cls):


if __name__ == '__main__':
    run = Controller()
    run.game()

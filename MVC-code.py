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
    def __init__(self):
        super().__init__()
        self.paddleY = 440
        self.paddleLeft = 310
        self.paddleWidth = 100
        self.paddleHeight = 10

        self.paddle_x_change = 0
        self.key_press = 0

        self.screenWidth = 640
        self.screenHeight = 400

        self.image = pygame.Surface([self.paddleWidth, self.paddleHeight])
        self.rect = self.image.get_rect()
        self.rect.x = (self.screenWidth- self.paddleWidth) / 2
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
        elif key_press == 2 and self.rect.x >= 580:
            self.rect.x = 580

class Ball(pygame.sprite.Sprite):
    angle = random.randrange(-45,45)
    speed = 8
    xcomp = 320
    ycomp = 432
    ballRadius = 8
    def __init__(self):
        super().__init__()
        self.p = Paddle()
        #self.ballRadius = 8
        #self.speed = 8 #MIGHT NOT NEED
        #self.angle = 180
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
            self.directionRad = math.radians(self.angle) #CONVERTS DIRECTION ANGLE TO RADIANS
            #self.xcomp = self.rect.x
            #self.ycomp = self.rect.y

            """ANGLE RADIAN CONVERSION TO SIN AND COS"""
            self.xcomp += self.speed * math.sin(self.directionRad)
            self.ycomp -= self.speed * math.cos(self.directionRad)

            """CHANGES X AND Y OF BALL COORDINATE"""
            self.rect.x = self.xcomp
            self.rect.y = self.ycomp

            """IF STATEMENTS FOR BALL REBOUND"""
            if self.ycomp <= 0:
                self.rebound(0)
                self.ycomp = 1
            if self.xcomp <= 0:
                self.angle = (360 - self.angle)
                self.xcomp = 1
            if self.xcomp > (self.screenWidth - self.ballRadius):
                self.angle = (360 - self.angle)
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

    pygame.init()

    displayDimensions = (640,480)
    gameDisplay = pygame.display.set_mode(displayDimensions)
    pygame.display.set_caption('Brick Ball!')

    bricks = pygame.sprite.Group()
    ballGroup = pygame.sprite.Group()
    allSprites = pygame.sprite.Group()

    p = Paddle()
    allSprites.add(p)

    b = Ball()
    allSprites.add(b)
    ballGroup.add(b)

    #bricks
    topBrick = 80
    bricksNum = 12
    Brick.build_bricks(bricks, bricksNum, topBrick, allSprites)

    typicalFont = pygame.font.SysFont('Helvetica', 80, bold = True)

    clock = pygame.time.Clock()

    # state = 0


    def __init__(self):
        super().__init__()
        """PYGAME INITIALIZATION"""
        #pygame.init()

        """CLASS INSTANCES"""
        # self.b = Ball()
        # self.p = Paddle()

        #self.brick = Brick(WHITE, 0,0)

        """WINDOW DIMENSIONS"""
        # self.displayDimensions = (640,480)
        # self.gameDisplay = pygame.display.set_mode(self.displayDimensions)
        # pygame.display.set_caption('Brick Ball!')

        """SPRITE GROUPS"""
        # self.bricks = pygame.sprite.Group()
        # self.ballGroup = pygame.sprite.Group()
        # self.allSprites = pygame.sprite.Group()

        # self.allSprites.add(self.p)

        # self.ballGroup.add(self.b)
        # self.allSprites.add(self.b)

        """BLOCK CREATION"""
        # topBrick = 80
        # bricksNum = 12
        # self.brick.build_bricks(self.bricks, bricksNum, topBrick, self.allSprites)

        #print(self.bricks)
        """FONT"""
        # self.typicalFont = pygame.font.SysFont('Helvetica', 80, bold = True)

        #LOGEN Edit
        self.state = 0

    def game(self):
        # clock = pygame.time.Clock()

        #self.state = 0
        gameExit = False
        key_press = 0

        """GAME LOOP"""
        while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    #gameExit = True

                """COLLISION HANDLING"""
            if pygame.sprite.spritecollide(self.p, self.ballGroup, False):
                control = (int(self.p.rect.x) + (self.p.paddleWidth / 2)) - (int(self.b.rect.x) + (self.b.ballRadius / 2))
                self.b.rect.y = 432
                self.b.rebound(control)

                #"""
                if not gameExit:
                    gameExit = self.b.update(self.state)

                if gameExit and len(self.bricks) != 0:#and b.rect.y < 440:
                    msg = self.typicalFont.render("LOST", 1, WHITE)
                    msgpos = msg.get_rect(centerx = 320)
                    msgBottom = 180
                    self.gameDisplay.blit(msg, msgpos)
                #"""

            hitBlocks = pygame.sprite.spritecollide(self.b, self.bricks, True)
            if len(hitBlocks) > 0:
                self.b.rebound(0)
            if len(hitBlocks) == 0:
                #gameExit = True
                winmsg = self.typicalFont.render('Winner Winner Chicken Dinner', 0, WHITE)
                winmsgpos = winmsg.get_rect(centerx = 400)
                winmsgBottom = 300
                self.gameDisplay.blit(winmsg, winmsgpos)

                # if event.type == pygame.KEYDOWN:
                #     if event.key == pygame.K_SPACE:
                #         if self.state == 1:
                #             self.b.update()
                #             print('Yea it works')

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
                print(3)
                print(self.b.speed)

            self.gameDisplay.fill(GREENISH)

            self.allSprites.draw(self.gameDisplay)

            self.p.rect.x += (self.p.paddle_x_change)

            self.b.update(self.state)

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit
        quit()

if __name__ == '__main__':
    run = Controller()
    run.game()

import pygame
import math
import random

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.paddleY = 440
        self.paddleLeft = 310
        self.paddleWidth = 100
        self.paddleHeight = 20

        self.speed = 0
        self.paddle_x_change = 0
        self.key_press = 0

        self.screenWidth = 640
        self.screenHeight = 400

        self.image = pygame.Surface([self.paddleWidth, self.paddleHeight])
        self.rect = self.image.get_rect()
        self.rect.x = 320
        self.rect.y = 440

    def movePaddle(self, key_press):
        """x = 1 is the left arrow
        x = 2 is the right arrow
        x = 3 is the spacebar"""

        if self.key_press == 0:
            self.paddle_x_change = 0
        if self.key_press == 1 and self.speed != 0:
            self.paddle_x_change = -5
        elif self.key_press == 1 and self.paddleLeft <= 0:
            self.paddle_x_change = 0

        elif (key_press == 2) and self.speed != 0:
            self.paddle_x_change = 5
        elif key_press == 2 and self.paddleLeft >= 580:
            self.paddle_x_change = 580

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.p = Paddle()
        self.ballRadius = 8
        self.ballPos = [342, 433]
        self.speed = 8.0 #MIGHT NOT NEED
        self.angle = 180
        self.screenWidth = 640

        self.image = pygame.Surface([self.ballRadius, self.ballRadius])
        self.rect = self.image.get_rect()

    def rebound(self, value):
        """REBOUNDS OR BOUNCES BALL OF OF WALL"""
        self.angle = (180 - self.angle) % 360
        self.angle -= value

    def update(self, xcomp, ycomp):
        """BALL LOCATION UPDATE"""
        self.directionRad = math.radians(self.angle) #CONVERTS DIRECTION ANGLE TO RADIANS
        self.xcomp = xcomp
        self.ycomp = ycomp

        """ANGLE RADIAN CONVERSION TO SIN AND COS"""
        self.xcomp += self.speed * math.sin(self.directionRad)
        self.ycomp -+ self.speed * math.cos(self.directionRad)

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
        if self.ycomp > 600:
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
    def build_bricks(cls, bricks, brk_num, brk_top, sprites):
        for i in range(5):
            rand_color = (255 * random.random(), 255 * random.random(), 255 * random.random())
            acolor = rand_color
            for j in range(1, brk_num):
                brick = cls(acolor, j * (cls.width + 2) + 1, brk_top)
                bricks.add(brick)
                sprites.add(brick)
            brk_top += cls.height + 2

class Controller(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        """PYGAME INITIALIZATION"""
        pygame.init()

        """COLORS"""
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.greenish = (0, 50, 50)
        self.blueish = (0, 255, 204)

        """CLASS INSTANCES"""
        self.b = Ball()
        self.p = Paddle()
        self.brick = Brick(self.white, 0,0)

        """WINDOW DIMENSIONS"""
        self.displayDimensions = (640,480)
        self.gameDisplay = pygame.display.set_mode(self.displayDimensions)
        pygame.display.set_caption('Brick Ball!')

        """SPRITE GROUPS"""
        self.brick.bricks = pygame.sprite.Group()
        self.ballGroup = pygame.sprite.Group()
        self.allSprites = pygame.sprite.Group()

        self.allSprites.add(self.p)

        self.ballGroup.add(self.b)
        self.allSprites.add(self.b)


        """BLOCK CREATION"""
        topBrick = 80
        bricksNum = 15
        self.brick.build_bricks(self.brick.bricks, bricksNum, topBrick, self.allSprites)


        """FONT"""
        typicalFont = pygame.font.SysFont('Helvetica', 80, bold = True)

    def game(self):
        clock = pygame.time.Clock()

        gameExit = False
        key_press = 0

        """GAME LOOP"""
        while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True

                """PADDLE CONTROL"""
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.b.speed == 0:
                        x = 1
                        self.p.movePaddle(x)
                    elif event.key == pygame.K_RIGHT and self.b.speed == 0:
                        x = 2
                        self.p.movePaddle(x)
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_SPACE or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                            x = 0
                            self.p.movePaddle(x)

                if not gameExit:
                    self.b.update(self.b.rect.x, self.b.rect.y)

                """COLLISION HANDLING"""
                if pygame.sprite.spritecollide(self.p, self.ballGroup, False):
                    control = (self.paddleRect.x + self.p.paddleWidth / 2) - (self.b.ballRect + self.b.ballRadius / 2)
                    self.b.ballPos[1] = self.gameDisplay.get_height() - self.p.paddleHeight - self.b.ballRadius - 1
                    self.b.rebound(self.control)

                hitBlocks = pygame.sprite.spritecollide(self.b, self.brick.bricks, True)
                if len(self.brick.bricks) > 0:
                    self.b.rebound(0)
                if len(self.brick.bricks) == 0:
                    gameExit = True
                    winmsg = typicalFont.render('Winner Winner Chicken Dinner', 0, white)
                    winmsgpos = winmsgpos.get_rect(centerx = 400)
                    winmsgBottom = 300
                    screen.blit(winmsg, winmsgPos)

            self.gameDisplay.fill(self.greenish)

            self.allSprites.draw(self.gameDisplay)
            self.ballGroup.draw(self.gameDisplay)

            self.p.rect.x += (self.p.paddle_x_change)

            pygame.display.update()
            clock.tick(60)

        pygame.quit
        quit()

if __name__ == '__main__':
    run = Controller()
    run.game()

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

        self.ballVelocity = 0
        self.paddleLeftChange = 0
        self.key_press = 0

        self.screenWidth = 640
        self.screenHeight = 400

    def movePaddle(self, key_press):
        """x = 1 is the left arrow
        x = 2 is the right arrow
        x = 3 is the spacebar"""

        if self.key_press == 0:
            self.paddleLeftChange = 0
        if self.key_press == 1 and self.ballVelocity != 0:
            self.paddleLeftChange = -5
        elif self.key_press == 1 and self.paddleLeft <= 0:
            self.paddleLeftChange = 0

        elif (key_press == 2) and self.ballVelocity != 0:
            self.paddleLeftChange = 5
        elif key_press == 2 and self.paddleLeft >= 580:
            self.paddleLeftChange = 580

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.p = Paddle()
        self.ballRadius = 8
        self.ballPos = [342, 433]
        self.ballVelocity = 8.0 #MIGHT NOT NEED
        self.screenWidth = 640

    def rebound(self, value):
        """REBOUNDS OR BOUNCES BALL OF OF WALL"""
        self.angle = (180 - self.angle) % 360
        self.angle -= value

    def update(self):
        """BALL LOCATION UPDATE"""
        self.diectionRad = math.radians(self.angle)#CONVERTS DIRECTION ANGLE TO RADIANS

        """ANGLE RADIAN CONVERSION TO SIN AND COS"""
        self.x += self.speed * math.sin(directionRad)
        self.y -+ self.speed * math.cos(directionRad)

        """CHANGES X AND Y OF BALL COORDINATE"""
        self.ballPos[0] = self.x
        self.ballPos[1] = self.y

        """IF STATEMENTS FOR BALL REBOUND"""
        if self.y <= 0:
            self.rebound(0)
            self.y = 1
        if self.x <= 0:
            self.angle = (360 - self.angle)
            self.x = 1
        if self.x > (self.screenWidth - self.ballRadius):
            self.angle = (360 - self.angle)
            self.x = (self.screenWidth - self.ballRadius) - 1
        if self.y > 600:
            return True
        else:
            return False

class Brick(pygame.sprite.Sprite):
    """CLASS FOR THE CREATION OF BLOCKS"""
    #Class variable
    width = 48
    height = 10

    def __init__(self, xcor, ycor):
        super().__init__()
        """INITIALIZES BLOCK COLOR AND COORDINATES"""
        # self.brickObj = pygame.draw.rect(gameDisplay, color, Brick.width, Brick.height)
        # self.brickObj.fill(color)
        # self.rect = self.image.get_rect()


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

            """CLASS INSTANCES"""
            self.b = Ball()
            self.p = Paddle()

            """WINDOW DIMENSIONS"""
            self.displayDimensions = (640,480)
            self.gameDisplay = pygame.display.set_mode(self.displayDimensions)
            pygame.display.set_caption('Brick Ball!')

            """COLORS"""
            self.white = (255, 255, 255)
            self.black = (0, 0, 0)
            self.greenish = (0, 50, 50)
            self.blueish = (0, 255, 204)

            """OBJECTS"""
            self.paddleObj = pygame.Surface([self.p.paddleWidth, self.p.paddleHeight])
            self.ballObj = pygame.Surface([self.b.ballRadius, self.b.ballRadius])
            self.brickObj = pygame.Surface([48, 10])

            self.paddleRect = self.paddleObj.get_rect()
            self.ballRect = self.ballObj.get_rect()
            self.brickRect = self.brickObj.get_rect()

            brick_xcor = self.brickRect.x
            brick_ycor = self.brickRect.y

            self.brick = Brick(brick_xcor, brick_ycor)




            """SPRITE GROUPS"""
            self.brick.bricks = pygame.sprite.Group()
            self.ballGroup = pygame.sprite.Group()
            self.allSprites = pygame.sprite.Group()

            self.allSprites.add(self.p)

            self.allSprites.add(self.b)
            self.ballGroup.add(self.b)

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
                    if event.key == pygame.K_LEFT and self.ballVelocity != [0,0]:
                        p.key_press = 1
                        p.movePaddle(x)
                    elif event.key == pygame.K_RIGHT and self.ballVelocity != [0,0]:
                        p.key_press = 2
                        p.movePaddle(x)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        p.key_press = 0
                        p.movePaddle(x)

                if not gameExit:
                    b.ballUpdate()

                """COLLISION HANDLING"""
                if pygame.sprite.spritecollide(p, ballGroup, False):
                    control = (self.paddleRect.x + p.paddleWidth / 2) - (b.ballPos[0] + b.ballRadius / 2)
                    b.ballPos[1] = gameDisplay.get_height() - p.paddleHeight - b.ballRadius - 1
                    b.rebound(control)

                # hitBlocks = pygame.sprite.spritecollide(self.b, self.brick, True)
                # if len(self.brick) > 0:
                #     ball.rebound(0)
                # if len(self.bricks) == 0:
                #     gameExit = True
                #     winmsg = typicalFont.render('Winner Winner Chicken Dinner', 0, white)
                #     winmsgpos = winmsgpos.get_rect(centerx = 400)
                #     winmsgBottom = 300
                #     screen.blit(winmsg, winmsgPos)
                # allSprites.draw(screen)

            gameDisply.fill(greenish)

            p.paddleLeft += (p.paddleLeftChange)
            paddleImage = pygame.Surface([p.paddleWidth, p.paddleHeight])
            paddleImage.fill(white)

            pygame.display.update()
            clock.tick(60)

            pygame.quit
            quit()

if __name__ == '__main__':
    run = Controller()
    run.game()

import pygame

class Paddle:
    def __init__(self):
        self.paddleY = 440
        self.paddleLeft = 310
        self.paddleWidth = 60
        self.paddleHeight = 12
        self.ballVelocity = [0,-0]
        self.paddleLeftChange = 0

    def movePaddle(self, x):
        """x = 1 is the left arrow
        x = 2 is the right arrow
        x = 3 is the spacebar"""

        if x == 0:
            self.paddleLeftChange = 0
        if x == 1:
            self.paddleLeftChange = -5
        elif x == 1 and self.paddleLeft <= 0:
            self.paddleLeftChange = 0

        elif (x == 2) and (self.paddleLeft < 580):
            self.paddleLeftChange = 5
        elif x == 2 and self.paddleLeft >= 580:
            self.paddleLeftChange = 580


class Ball:
    def __init__(self):
        self.ballRadius = 8
        self.ballPos = [342, 433]
        self.ballVelocity = [5, -5]

    def ballMovement(self):
        if self.ballLeft == 0:
            self.ballLeft = 0
            self.ballVelocity[0] = -self.ballVelocity[0]

        if self.ballLeft == 636:
            self.ballLeft = 636
            self.ballVelocity[0] = -self.ballVelocity[0]

        if self.ballY <= 0:
            self.ballY = 0
            self.ballVelocity[1] = -self.ballVelocity[1]

    def ballUpdate(self):
        self.ballPos[0] += self.ballVelocity[0]
        self.ballPos[1] += self.ballVelocity[1]


class Blocks:
    def __init__(self):
        self.blocks = []

    def createBlocks(self):
        y = 10
        for y in range(y, 250, 27):
            x = 5
            for x in range(x, 615, 32):
                self.blocksX = x
                self.blocksY = y
                self.blockLength = 30
                self.blocksHeight = 25
                newBrick = (self.blocksX, self.blocksY, self.blockLength, self.blocksHeight)
                self.blocks.append(newBrick)

class Controller:

    def __init__(self):
        self.p = Paddle()
        self.b = Ball()
        self.block = Blocks()
        self.blocks = Blocks()

        self.blocks.createBlocks()

        self.ballVelocity = [0,0]

        self.state = 0

    def game(self):
        p = Paddle()
        b = Ball()

        pygame.display.init()
        pygame.font.init()

        white = (255,255,255)
        black = (0,0,0)
        brickColor = (51,102,255)

        screensize = (640,480)
        screen = pygame.display.set_mode(screensize)


        gameExit = False
        clock = pygame.time.Clock()
        x = 0

        """PADDLE MOVEMENT CONTROL"""
        while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.ballVelocity != [0,0]:
                        x = 1
                        p.movePaddle(x)

                    elif event.key == pygame.K_RIGHT and self.ballVelocity != [0,0]:
                        x = 2
                        p.movePaddle(x)

                    elif event.key == pygame.K_SPACE:
                        self.ballVelocity = [5,5]
                        self.state = 1  #PLAYING

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x = 0
                        p.movePaddle(x)

            screen.fill(white)

            p.paddleLeft += (p.paddleLeftChange) % 640
            paddle = pygame.draw.rect(screen, black, [p.paddleLeft, p.paddleY, p.paddleWidth, p.paddleHeight])

            if self.state == 1:
                b.ballUpdate()
            ball = pygame.draw.circle(screen, black, b.ballPos, b.ballRadius)

            for i in self.blocks.blocks:
                bricks = pygame.draw.rect(screen, brickColor, list(i))

            pygame.display.update()
            clock.tick(60)




        pygame.quit()
        quit()

if __name__ == '__main__':
    run = Controller()
    run.game()

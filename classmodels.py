class Paddle:
    def __init__(self):
        self.paddleY = 440
        self.paddleLeft = 310
        self.paddleWidth = 60
        self.paddleHeight = 12
        self.ballVelocity = [0,-0]

    def movePaddle(self, x):

        """x = 1 is the left arrow
        x = 2 is the right arrow
        x = 3 is the spacebar"""

        if x == 1 and self.paddleLeft > 0:
            self.paddleLeft -= 5
        elif x == 1 and self.paddleLeft == 0:
            self.paddleLeft = 0

        elif (x == 2) and (self.paddleLeft < 580):
            self.paddleLeft += 5
        elif x == 2 and self.paddleLeft == 580:
            self.paddleLeft = 580

        elif x == 3:
            self.ballVelocity = [5, -5]
            """state gets changed in controller"""

class Ball:
    def __init__(self):
        self.ballLeft = 300
        self.ballDiameter = 16
        self.ballY = 424
        self.ballRadius = 8
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
        self.ballLeft += self.ballVelocity[0]
        self.ballY += self.ballVelocity[1]


class Blocks:
    def __init__(self):
        self.blocks = []

    def createBlocks(self):
        y = 250
        for y in range(y, 451, 27):
            x = 5
            for x in range(x, 636, 32):
                self.blocksX = x
                self.blocksY = y
                self.blockLength = 30
                self.blocksHeight = 25
                newBrick = (self.blocksX, self.blocksY) #self.blockLength, self.blocksHeight)
                self.blocks += newBrick


"""---basic main loop---
while(True):
    for events in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ---inset all functions---
    pygame.display.flip()"""

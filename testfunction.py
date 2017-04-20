import classmodels

def test():
    model = classmodels

    """tests for Paddle class"""

    paddle = model.Paddle()
    print('PADDLE TEST')
    print(paddle.paddleLeft)

    x = 1
    paddle.movePaddle(x)
    print(paddle.paddleLeft)
    paddle.movePaddle(x)
    print(paddle.paddleLeft)

    x = 2
    paddle.movePaddle(x)
    print(paddle.paddleLeft)
    paddle.movePaddle(x)
    print(paddle.paddleLeft)

    print(paddle.ballVelocity)
    x = 3
    paddle.movePaddle(x)
    print(paddle.ballVelocity)

    print('\nMOVEMENT BOUND TEST')
    """---If an unregistered number is entered, nothing happens---"""
    for i in range(70):
        paddle.movePaddle(3)
        print(paddle.paddleLeft)

    """Tests for Ball class"""

    ball = model.Ball()
    print('\nBALL TEST')
    print(ball.ballLeft)
    print(ball.ballY)
    print(ball.ballVelocity)

    ball.ballLeft = 0
    ball.ballMovement()
    print(ball.ballLeft)
    print(ball.ballVelocity[0])

    ball.ballLeft = 636
    ball.ballMovement()
    print(ball.ballLeft)
    print(ball.ballVelocity[0])

    ball.ballY = 0
    ball.ballMovement()
    print(ball.ballY)
    print(ball.ballVelocity[1])

    print('\nTEST FOR BALL UPDATE')
    ball.ballLeft =300
    print('original Left value: 300')
    ball.ballY = 424
    print('original Left value: 424')
    ball.ballVelocity = [5,-5]
    for i in range(5):
        ball.ballUpdate()
        print(ball.ballLeft)
        print(ball.ballY)

    """TEST FOR BLOCKS CLASS"""
    print('\nBLOCKS TEST')
    blocks = model.Blocks()
    blocks.createBlocks()
    print(blocks.blocks)

test()

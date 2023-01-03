from turtle import Screen
from paddle import PongPaddle
from net import PongNet

screen = Screen()

screen.setup(width=1000, height=500)
screen.title("PONG")
screen.bgcolor('black')

net = PongNet(screen)
net.draw_net()

paddle_A = PongPaddle(screen, 'A')
paddle_B = PongPaddle(screen, 'B')

screen.exitonclick()

import os
os.system('cls')


# main program
from turtle import Screen
from paddle import Paddle
from line import Create_Line
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.cv._rootwindow.resizable(False, False) #This is not documented

screen.bgcolor('black')
screen.setup(width=800, height=600, startx=10)
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0), 'Blue')
l_paddle = Paddle((-350, 0), 'DeepPink')

create_line = Create_Line()

ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')

screen.onkeypress(l_paddle.go_up, 'w')
screen.onkeypress(l_paddle.go_down, 's')

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)

    screen.update()
    ball.move()
    

    # Detect collision whit wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance((l_paddle)) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.r_point()

    #Detect L paddle misses
    if ball.xcor() < - 380:
        ball.reset_position()
        scoreboard.l_point()
    
    scoreboard.update_scoreboard()

    

screen.exitonclick()
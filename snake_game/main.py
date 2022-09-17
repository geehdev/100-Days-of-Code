from os import system
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

system('cls')


""" Snake Game: Jogo da Cobra
    POO: Inheritance & List Slicing // Programação Orientada a Objetos: Herança & Fatiamento de Lista."""

# programa principal
screen = Screen()
screen.cv._rootwindow.resizable(False, False) #This is not documented
screen.setup(width=600, height=600, startx=100)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down , 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right , 'Right')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    #Detect collision with wall.
    if snake.head.xcor() > 289 or snake.head.xcor() < -289 or snake.head.ycor() > 289 or snake.head.ycor() < -289:
        scoreboard.reset()
        snake.reset_snake()

    #Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset_snake()
    
            
screen.exitonclick()
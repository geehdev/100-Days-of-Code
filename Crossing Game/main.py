import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.cv._rootwindow.resizable(False, False) #This is not documented
screen.setup(width=600, height=600, startx=100)
screen.tracer(0)
screen.bgcolor('LightSkyBlue')

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()
    
    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Detect successful crossing
    if player.is_at_finish_line():
        player.go_tu_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()
from turtle import Turtle

# constants
STARTING_POSITION = (0, -280)
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__(visible=False)
        # self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-290, 250)
        self.update_score()
        

    def update_score(self):
        self.clear()
        self.write(f'Level: {self.level}', font=FONT)


    def increase_level(self):
        self.level += 1
        self.update_score()
  

    def game_over(self):
        self.goto(8, 0)
        self.write('GAME OVER', align='center',font=FONT)

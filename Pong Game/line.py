from turtle import Turtle

class Create_Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, -300)
        self.width(2)

        self.line()


    def line(self):
        for position in range(-305, 640, 30):
            self.pendown()
            self.goto(0, position)
            self.penup()
            self.goto(0, position + 20)

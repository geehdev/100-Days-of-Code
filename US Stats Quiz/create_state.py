from turtle import Turtle

class Write_State:
    def __init__(self, name_state, coordenation):
        self.tartaruga = Turtle()
        self.tartaruga.hideturtle()
        self.tartaruga.penup()
        self.tartaruga.setpos(coordenation)
        self.tartaruga.write(name_state)
    
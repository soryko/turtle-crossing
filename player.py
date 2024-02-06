from turtle import Turtle

class Player(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(position)
    
    def go_up(self):
        new_y = self.ycor() + 10
        self.goto(0, new_y)
    
    def go_down(self):
        new_y = self.ycor() - 10
        self.goto(0, new_y)
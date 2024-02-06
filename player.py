from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
    
    def go_up(self):
        new_y = self.ycor()
    
    def go_down(self):
        new_y = self.ycor()
from turtle import Turtle

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.color("green")
        self.penup()
        self.x_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor()
        self.goto(new_x, self.ycor())


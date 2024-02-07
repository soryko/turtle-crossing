from turtle import Turtle

class CarManager(Turtle):

    def __init__(self, rand_speed):
        super().__init__()
        self.color("green")
        self.penup()
        self.x_move = -10
        self.move_speed = 0.1 * rand_speed

    def move(self):
        new_x = self.xcor() + self.x_move
        self.goto(new_x, self.ycor())

    def reset_position(self, rand_y):
        self.goto(250, rand_y)
        self.move_speed = .1 * rand_y
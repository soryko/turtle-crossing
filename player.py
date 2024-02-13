from turtle import Turtle

STARTING_POSITION = (0,-250)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape('turtle')
        self.penup()
        self.go_to_start()
        self.setheading(90)
    
    def go_up(self):
        new_y = self.ycor() + 10
        self.goto(0, new_y)
    
    def go_down(self):
        new_y = self.ycor() - 10
        self.goto(0, new_y)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else :
            return False
        
    def go_to_start(self):
        self.goto(STARTING_POSITION)
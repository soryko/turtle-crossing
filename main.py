import time 
from turtle import Screen
from player import Player
from car_manager import CarManager
#from scoreboard import Scoreboard

#create screen
screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

#moving objects
player = Player((0,0))
cars = CarManager()


#refresh screen
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()



screen.exitonclick()
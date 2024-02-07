import time 
from turtle import Screen
from player import Player
from car_manager import CarManager
import random
#from scoreboard import Scoreboard

#create screen
screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

#moving objects
player = Player((0,0))
player.left(90)


#movement options up/down only

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

num_cars = random.randint(1,5)


#refresh screen
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #generate random cars going right to left
    for cars in range(num_cars):
        rand_speed = (random.randint(1,3))/2
        cars = CarManager(rand_speed)
        rand_y = random.randint(50,250)
        cars.reset_position(rand_y)
        cars.left(180)
        cars.move()
    #implement collision if statements

    #scoreboard



screen.exitonclick()
import time 
from turtle import Screen
from player import Player
from car_manager import CarManager

from scoreboard import Scoreboard

#create screen
screen = Screen()
screen.bgcolor('white')
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

#moving objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
#movement options up/down only

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")



#refresh screen
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #generate random cars going right to left
    car_manager.create_cars()
    car_manager.move_cars()
    #implement collision if statements
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    #scoreboard
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
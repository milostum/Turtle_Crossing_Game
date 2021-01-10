import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#      []         {}

player = Player()
scoreboard = Scoreboard()

car = CarManager()
car.hideturtle()
cars_positions = car.cars_positions

cars = []
for car_position in cars_positions:
    car = CarManager()
    car.cars_random()
    car.goto(car_position)
    cars.append(car)

screen.listen()
screen.onkey(fun=player.go_up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    for car in cars:
        car.car_move()
        if car.xcor() < -300:
            car.cars_random()
            car.goto(280, randint(-260, 280))

        if player.ycor() > player.finish:
            player.level_start()
            scoreboard.level_up()
            for car_ in cars:
                car_.level_up()

        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()

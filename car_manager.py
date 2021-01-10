from turtle import Turtle
from random import choice, randint


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
NUMBER_OF_CARS = 25


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.car_speed = STARTING_MOVE_DISTANCE
        self.cars_positions = []
        self.cars_position()

    def car_move(self):
        self.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

    def cars_random(self):
        self.color(choice(COLORS))

    def cars_position(self):
        for i in range(NUMBER_OF_CARS):
            self.cars_positions.append((randint(-280, 280), randint(-260, 280)))

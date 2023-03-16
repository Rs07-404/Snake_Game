import turtle
from turtle import Turtle
import random

VALID_POSITIONS = [-240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100, 120, 140,
                   160, 180, 200, 220, 240]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color("white")
        self.penup()
        self.shapesize(1)
        self.food_x = self.xcor()
        self.food_y = self.ycor()
        self.change_position()

    def check_food_coordinates(self):
        self.food_x = self.xcor()
        self.food_y = self.ycor()
        food_coordinates = (self.food_x, self.food_y)
        return food_coordinates

    def change_position(self):
        food_x = random.choice(VALID_POSITIONS)
        food_y = random.choice(VALID_POSITIONS)
        self.goto(food_x, food_y)

    def change_color(self):
        r = random.randint(10, 255)
        g = random.randint(10, 255)
        b = random.randint(10, 255)
        turtle.colormode(255)
        self.color(r, g, b)

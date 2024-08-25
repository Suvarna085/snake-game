from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.shapesize(0.5, 0.5)

    def food_position(self):
        new_x = random.randint(-280, 280)
        new_y = random.randint(-280, 280)
        self.penup()
        self.goto(new_x, new_y)





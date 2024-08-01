from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-380, 380)
        random_y = random.randint(-380, 380)
        self.penup()
        self.goto(random_x, random_y)

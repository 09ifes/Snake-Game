from turtle import Screen, Turtle
import random

segments = []
starting_positions = [(0, 0), (-20, 0), (-40, 0), (-60, 0)]


def build_snake():
    """Snake = list of turtle objects"""
    for position in starting_positions:
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        segments.append(new_segment)


class Snake:
    def __init__(self):
        build_snake()
        self.heading = segments[0].heading()

    def create_food(self):
        """Creates food object and places randomly"""
        self.food = Turtle('square')
        self.food.shapesize(1,1,1)
        self.food.penup()
        self.food.color('yellow')
        self.x = random.randrange(-280, 280, 20)
        self.y = random.randrange(-280,280, 20)
        self.food.goto(self.x, self.y)

    def change_food(self):
        self.x = random.randrange(-280, 280, 20)
        self.y = random.randrange(-280, 280, 20)
        self.food.goto(self.x, self.y)

    def grow(self):
        """Adds more segments to the snake"""
        new_segment = Turtle('square')
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)
        self.length = len(segments)
        x = segments[self.length - 2].xcor()
        y = segments[self.length - 2].ycor()
        segments[self.length - 1].goto(x, y)

    def go_up(self):
        if self.heading == 270:
            pass
        else:
            segments[0].setheading(90)
            self.heading = segments[0].heading()

    def go_down(self):
        if self.heading == 90:
            pass
        else:
            segments[0].setheading(270)
            self.heading = segments[0].heading()

    def go_left(self):
        if self.heading == 0:
            pass
        else:
            segments[0].setheading(180)
            self.heading = segments[0].heading()

    def go_right(self):
        if self.heading == 180:
            pass
        else:
            segments[0].setheading(0)
            self.heading = segments[0].heading()

    def reset(self):
        for n in segments:
            n.goto(1000,1000)
        segments.clear()
        build_snake()
        self.change_food()
        self.heading = segments[0].heading()



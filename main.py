from turtle import Screen, Turtle
from snake import Snake, segments, build_snake
import time
from scoreboard import Scores

"""Creates and configures screen"""
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
score = 0
scores = Scores()
controls = [screen.onkey(snake.go_up, "Up"), screen.onkey(snake.go_down, "Down"), screen.onkey(snake.go_left, "Left"), screen.onkey(snake.go_right, "Right")]

screen.listen()

snake.create_food()


def reset():
    snake.reset()
    scores.new_high()
    scores.reset()
    #screen.update()

game = True


while game:
    length = len(segments)
    """To achieve the snake movement, the segments move individually, from bottom to top (the last segment goes to the
     position of the next segment up, and so on)"""
    for seg in range(length-1, 0, -1):
        x = segments[seg-1].xcor()
        y = segments[seg-1].ycor()
        segments[seg].goto(x, y)
    segments[0].forward(20)  # First segment moves after the preceding ones have

    """The 2 if statements below determine what happens when the snake collides with the boundary, and the food"""
    if (snake.x - 0.5) < segments[0].xcor() < (snake.x + 0.5) and (snake.y - 0.5) < segments[0].ycor() < (snake.y + 0.5):
        snake.grow()
        snake.change_food()
        scores.score += 1
        scores.text()
    if segments[0].xcor() <= -300 or segments[0].xcor() == 300 or segments[0].ycor() <= -300 or segments[0].ycor() >= 300:
        reset()
    length = len(segments)
    """Resets when snake collides with itself (if any segment's position is the same as another segment's)"""
    for seg in range(length-1, 0, -1):
        if segments[0].xcor() == segments[seg].xcor() and segments[0].ycor() == segments[seg].ycor():
            reset()


    screen.update()            # Update method used so that the motion of the snake appears fluid
    time.sleep(0.4)

scores.reset()


screen.exitonclick()





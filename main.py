from turtle import Screen
from snake import Snake
import time
from scoreboard import ScoreBoard
from food import Food
screen = Screen()
screen.setup(width=800, height=800)
screen.tracer(0)
screen.listen()
snake = Snake()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

scoreboard = ScoreBoard()
food = Food()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

    #Contact with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.level_up()
        snake.extend()

    #Contact with wall
    if snake.head.xcor() > 390 or snake.head.xcor() < -390 or snake.head.ycor() > 390 or snake.head.ycor() < -390:
        scoreboard.update_high_score()
        snake.refresh()

    #Contact with tail
    for seg in snake.segment[1:]:
        if snake.head.distance(seg) < 10:
            snake.refresh()

screen.exitonclick()
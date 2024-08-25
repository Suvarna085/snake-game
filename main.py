from turtle import Turtle, Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left_snake, "Left")
screen.onkey(snake.right_snake, "Right")
game_is_on = True
food.food_position()
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    if snake.head.distance(food)<15:
        food.food_position()
        snake.extend()
        scoreboard.increase_score()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.score_reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            scoreboard.score_reset()
            snake.reset()

screen.exitonclick()
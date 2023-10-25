from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

snake.start_listening()

on = True
while on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    snake.start_listening()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.refresh()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        on = False

    for segment in snake.segments[1:-1]:
        if snake.head.distance(segment) < 10:
            on = False
            break

scoreboard.game_over()

screen.exitonclick()

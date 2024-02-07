from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

special_food_timer = time.time()


game_is_on = True
missed = False
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Crear comida especial si la serpiente ha alcanzado una longitud múltiplo de 5 y no se ha fallado en recogerla antes
    if len(snake.segments) % 5 == 0 and not food.is_special and not missed:
        food.special_food()
        special_food_timer = time.time()

    # Verificar si ha pasado el tiempo límite para recoger la comida especial
    if food.is_special and time.time() - special_food_timer >= 5:
        food.reset_special_food()
        missed = True
    # Detect collision with food
    if snake.head.distance(food) < 15:
        if food.is_special:
            scoreboard.increase_score(random.randint(1, 3))
            food.reset_special_food()
            missed = False
        else:
            scoreboard.increase_score(1)
            missed = False
        food.refresh()  # Refresh position of food
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        food.reset_special_food()

        # Detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
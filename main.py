import turtle
from turtle import Screen
from snake import Snake
import time
from food import Food
from scorecard import Scorecard

#screen setup
screen= Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

snake=Snake()
food = Food()
scorecard = Scorecard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision on of snake head with food
    if snake.snake_head.distance(food)<15:
        food.refresh()
        snake.extend_segment()
        scorecard.increase_score()
    #detect collision with wall
    if snake.snake_head.xcor() > 290 or snake.snake_head.xcor() < -290 or snake.snake_head.ycor()>290 or snake.snake_head.ycor() < -290:
        game_on=False
        scorecard.game_over()

    #Detect collision with snake body
    for segment in snake.snake_segment[1:]:
        if snake.snake_head.distance(segment)<5:
            game_on=False
            scorecard.game_over()
screen.exitonclick()


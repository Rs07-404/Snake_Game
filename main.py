# Name: Raunak Shah


from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score_board import Score_Board
import time
# Objects
screen = Screen()
screen.setup(height=600, width=600)

game_on = True
color = screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

# Front main Object
snake = Snake()
food = Food()
score_board = Score_Board()

# Border Object
border = Turtle()
border.hideturtle()
border.color("white")
border.width(1)
border.penup()
border.goto(x=260, y=-260)
border.pendown()
for _ in range(4):
    border.left(90)
    border.forward(520)

screen.listen()
screen.onkey(snake.up, key="Up", )
screen.onkey(snake.down, key="Down", )
screen.onkey(snake.left, key="Left", )
screen.onkey(snake.right, key="Right", )
# Game
while game_on:
    score_board.show_score_board()
    screen.update()
    snake.move()
    if snake.head.distance(food) < 2:
        snake.increase_length()
        score_board.increase_score()
        food.change_color()
        food.change_position()
    for seg in snake.segments:
        if (seg.ycor() > 250 or seg.xcor() > 250 or
            seg.ycor() < -250 or seg.xcor() < -250) and \
                (300 > seg.xcor() > -300 and 300 > seg.ycor() > -300):
            print("Wall")
            score_board.reset()
            snake.reset()
            time.sleep(1)
        else:
            for segment in (snake.segments[1:]):
                if snake.head.distance(segment) < 10 and (300 > segment.xcor() > -300 and 300 > segment.ycor() > -300):
                    print("Snake")
                    score_board.reset()
                    snake.reset()
                    time.sleep(1)
    time.sleep(0.14)
else:
    score_board.show_final_score()

screen.exitonclick()

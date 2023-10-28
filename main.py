from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from ai_paddle import AI_Paddle  # Import the AI_Paddle class
from center_line import CenterLine  # Import the CenterLine class
##################PONG GAME################
# 1. Create screen
# 2. Create paddles
#    - width = 20
#    - height = 100
#    - x_pos = 350
#    - y_pos = 0
#
# 3. Create a ball
# 4. Detect collision with wall and bounce
# 5. Detect collision with paddle
##########################################

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)  # hide animation e.g. of paddle move to side

# Create the center line
center_line = CenterLine()

r_paddle = Paddle((350, 0))
#l_paddle = Paddle((-350, 0))
l_paddle = AI_Paddle((-350, 0))  # Create an AI-controlled paddle on the left

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    #time.sleep(0.1)
    time.sleep(ball.move_speed)  # created attribute in ball class
    screen.update()
    ball.move()

    # Update the AI-controlled paddle's position based on the ball's position
    l_paddle.move_towards_ball(ball)

    # check if hit top or bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        # want to bounce differently then original bounce
        ball.bounce_x()

    # Detect when R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect when L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
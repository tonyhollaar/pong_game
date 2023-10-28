from paddle import Paddle


class AI_Paddle(Paddle):
    def move_towards_ball(self, ball):
        if self.ycor() < ball.ycor():
            self.go_up()
        elif self.ycor() > ball.ycor():
            self.go_down()
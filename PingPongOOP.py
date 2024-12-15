import turtle


class Paddle(turtle.Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_position, 0)

    def move_up(self):
        y = self.ycor()
        y += 20
        self.sety(y)

    def move_down(self):
        y = self.ycor()
        y -= 20
        self.sety(y)


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(0, 0)
        self.dx = 0.15
        self.dy = -0.15

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.score_1 = 0
        self.score_2 = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Player 1: {self.score_1} Player 2: {self.score_2}", align="center", font=("Courier", 24, "normal"))

    def player_1_score(self):
        self.score_1 += 1
        self.update_scoreboard()

    def player_2_score(self):
        self.score_2 += 1
        self.update_scoreboard()


class PingPongGame:
    def __init__(self):
        self.window = turtle.Screen()
        self.window.title("PingPongGame")
        self.window.bgcolor("blue")
        self.window.setup(width=800, height=600)
        self.window.tracer(0)

        # Creating paddles, ball, and scoreboard
        self.paddle_1 = Paddle(-350)
        self.paddle_2 = Paddle(350)
        self.ball = Ball()
        self.scoreboard = Scoreboard()

        # Setting up keyboard bindings
        self.window.listen()
        self.window.onkeypress(self.paddle_1.move_up, "w")
        self.window.onkeypress(self.paddle_1.move_down, "s")
        self.window.onkeypress(self.paddle_2.move_up, "Up")
        self.window.onkeypress(self.paddle_2.move_down, "Down")
        self.window.onkeypress(self.exit_game, "q")  # Press 'q' to quit the game

    def exit_game(self):
        self.window.bye()

    def check_collision(self):
        # Paddle and ball collisions
        if (self.ball.xcor() > 340 and self.ball.xcor() < 350) and (
                self.ball.ycor() < self.paddle_2.ycor() + 50 and self.ball.ycor() > self.paddle_2.ycor() - 40):
            self.ball.setx(340)
            self.ball.dx *= -1

        if (self.ball.xcor() < -340 and self.ball.xcor() > -350) and (
                self.ball.ycor() < self.paddle_1.ycor() + 50 and self.ball.ycor() > self.paddle_1.ycor() - 40):
            self.ball.setx(-340)
            self.ball.dx *= -1

    def check_border(self):
        # Border collisions
        if self.ball.ycor() > 290:
            self.ball.sety(290)
            self.ball.dy *= -1

        if self.ball.ycor() < -290:
            self.ball.sety(-290)
            self.ball.dy *= -1

        if self.ball.xcor() > 390:
            self.ball.goto(0, 0)
            self.ball.dx *= -1
            self.scoreboard.player_1_score()

        if self.ball.xcor() < -390:
            self.ball.goto(0, 0)
            self.ball.dx *= -1
            self.scoreboard.player_2_score()

    def play(self):
        while True:
            self.window.update()

            # Move the ball
            self.ball.move()

            # Check for collisions with the paddle and borders
            self.check_collision()
            self.check_border()


# Starting the game
if __name__ == "__main__":
    game = PingPongGame()
    game.play()

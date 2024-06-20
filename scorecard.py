from turtle import Turtle

class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.high_score=0
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=("Ariel",18,"normal"))
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Ariel", 18, "normal"))

    def game_over(self):
        print(f"Game Over! {self.score}")
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()


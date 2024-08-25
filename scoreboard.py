from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        with open("data.text") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Current Score: {self.current_score}  High Score : {self.high_score}", False, align="center", font=("Arial", 14, "normal"))
    def increase_score(self):
        self.current_score += 1
        self.update_score()
    def score_reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
        with open("data.text",mode='w') as file:
            file.write(f"{self.high_score}")
        self.current_score = 0
        self.update_score()
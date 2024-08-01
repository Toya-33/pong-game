from turtle import Turtle

FONT = ("Courier", 24, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("snake/high_score.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.goto(0, 340)
        self.update()
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", move=False, align="Center", font=FONT)

    def level_up(self):
        self.score += 1
        self.update()

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snake/high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update()

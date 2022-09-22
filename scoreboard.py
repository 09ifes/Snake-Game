from turtle import Turtle, Screen




class Scores(Turtle):
    """Sets up the displaying of scores/text on screen"""
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as file:
            self.high_score = file.read()
        self.high_score = 0
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.write(f'Score: {self.score}  High Score: {self.high_score}', True, align='center', font=('Arial', 20, 'normal'))
        self.hideturtle()


    def text(self):
        self.clear()
        self.penup()
        self.goto(0,270)
        self.color('white')
        self.write(f'Score: {self.score}  High Score: {self.high_score}', True, align='center', font=('Arial', 20, 'normal'))
        self.hideturtle()

    def new_high(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open('data.txt', mode='w') as file:
            file.write(f'{self.high_score}')
        self.score = 0
        self.text()

    def reset(self):
        self.clear()
        self.penup()
        self.goto(0, 270)
        self.color('white')
        self.write(f'Score: {self.score}  High Score: {self.high_score}', True, align='center', font=('Arial', 20, 'normal'))
        self.hideturtle()



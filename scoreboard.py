from turtle import Turtle
ALIGNMENT_OF_SCOREBOARD = 'center'
FONT_OF_SCOREBOARD = ('Arial', 15, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(0, 275)
        self.write(f'Score: {self.score}', align=ALIGNMENT_OF_SCOREBOARD, font=FONT_OF_SCOREBOARD)

    def refresh(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', align=ALIGNMENT_OF_SCOREBOARD, font=FONT_OF_SCOREBOARD)
        
    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT_OF_SCOREBOARD, font=FONT_OF_SCOREBOARD)
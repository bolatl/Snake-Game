from turtle import Turtle, Screen

Starting_positions = [(0, 0), (-20, 0), (-40, 0)]
Move_distance = 20
Up = 90
Down = 270
Left = 180
Right = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.screen = Screen()

    def create_snake(self):
        for position in Starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(Move_distance)

    def start_listening(self):
        self.screen.onkey(self.up, "Up")
        self.screen.onkey(self.down, "Down")
        self.screen.onkey(self.left, "Left")
        self.screen.onkey(self.right, "Right")
        self.screen.listen()

    def stop_listening(self):
        self.screen.onkey(None, "Up")
        self.screen.onkey(None, "Down")
        self.screen.onkey(None, "Left")
        self.screen.onkey(None, "Right")

    def up(self):
        if self.head.heading() != Down:
            self.head.setheading(90)
            self.stop_listening()

    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(270)
            self.stop_listening()

    def left(self):
        if self.head.heading() != Right:
            self.head.setheading(180)
            self.stop_listening()

    def right(self):
        if self.head.heading() != Left:
            self.head.setheading(0)
            self.stop_listening()

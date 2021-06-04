from turtle import Turtle


STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self):
        self.__snake = []
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        self.head = self.__snake[0]
        self.head.color("blue")
    

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.up()
        segment.goto(position)
        self.__snake.append(segment)


    def move(self):
        for seg_num in range(len(self.__snake)-1, 0, -1):
            new_x = self.__snake[seg_num - 1].xcor()
            new_y = self.__snake[seg_num - 1].ycor()
            self.__snake[seg_num].goto(new_x, new_y)
        
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    
    def grow(self):
        self.add_segment(self.__snake[-1].position())


    def self_collision(self):
        for any in self.__snake[1:]:
            if self.head.distance(any)<10:
                return True
        return False


#player.py

from turtle import Turtle

# 乌龟起点
STARTING_POSITION = (0, -120)

#RIGHT_POSITION = ()

#LEFT_POSITION

# 移动举例
MOVE_DISTANCE = 30

# 终点线
FINISH_LINE_Y = 140


class Player(Turtle):

    def __init__(self):

        super().__init__()

        # 导入乌龟图
        self.shape("turtle.gif")

        #self.color("black")

        self.penup()

        self.goto(STARTING_POSITION)

        self.setheading(90)

    # 乌龟上移
    def move_up(self):

        self.setheading(90)

        print(self.xcor(), self.ycor())

        self.forward(MOVE_DISTANCE)

        print(self.xcor(),self.ycor())

    # 乌龟左移
    def move_left(self):

        self.setheading(180)

        print(self.xcor(), self.ycor())

        self.forward(MOVE_DISTANCE)

        print(self.xcor(),self.ycor())

    # 乌龟右移
    def move_right(self):

        self.setheading(0)

        print(self.xcor(), self.ycor())

        self.forward(MOVE_DISTANCE)

        print(self.xcor(),self.ycor())

    # 乌龟回来起点
    def restart(self):

        self.goto(STARTING_POSITION)

        self.setheading(90)

    # 乌龟左越界
    def right(self):

        self.goto((130, self.ycor()))

        self.setheading(180)

    # 乌龟右越界
    def left(self):

        self.goto((-130, self.ycor()))

        #self.goto(STARTING_POSITION)

        self.setheading(0)
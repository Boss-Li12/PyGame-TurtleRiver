# car_manager.py

from turtle import Turtle

import random


#COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

# 移动位置和增量设置
STARTING_MOVE_DISTANCE = 5

MOVE_INCREMENT = 10



class CarManager(Turtle):

    def __init__(self, _carspeed):

        super().__init__()

        #self.color(random.choice(COLORS))

        # 导入“车”图片
        self.shape("shark.gif")

        self.shapesize(stretch_len=1, stretch_wid=1)

        self.setheading(180)

        self.penup()

        self.goto(130, random.randint(-3, 3) * 30)

        self.carspeed = _carspeed

    # ”车”移动
    def move(self):

        self.forward(STARTING_MOVE_DISTANCE)


    #def speedup(self):

        #self.carspeed /= 10

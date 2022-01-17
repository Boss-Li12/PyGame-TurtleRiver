# main.py

import time

from turtle import Screen

from player import Player

from car_manager import CarManager

from scoreboard import Scoreboard

# flag用来标记是否按下空格
flag = False

# 按下空格对应的处理函数
def start():

    global flag

    flag = True

# 初始化窗体
screen = Screen()

# 窗体宽高
screen.setup(width=300, height=300)

screen.tracer(0)

# 引入背景图片
screen.bgpic("background.gif")

# 引入“车”图片
screen.register_shape("shark.gif")

# 引入乌龟图片
screen.register_shape("turtle.gif")

# 定义玩家（乌龟）
player = Player()

# 车队列
cars=[]

# 当前车速
carspeednow = 0.1

# 初始化车类
car = CarManager(carspeednow)

# 加入车队列
cars.append(car)

# 初始化得分面板
scoreboard = Scoreboard()

# 监听窗体
screen.listen()

# 窗体标题
screen.title("按空格开始")

# 窗体监听的按钮
screen.onkey(start, "space")

screen.onkey(player.move_up, "Up")

screen.onkey(player.move_left, 'Left')

screen.onkey(player.move_right, 'Right')

# 计数器
count = 0


# 游戏是否结束
game_is_on = True


while game_is_on:

    count += 1

    print(car.carspeed)

    # 用来更新不同等级的车速
    time.sleep(car.carspeed)

    screen.update()

    # 未按空格车不走
    if flag == False:

        continue

    # 20个单位来一个新车
    if count % 20 == 0:

        car = CarManager(carspeednow)

        cars.append(car)

        #print(cars[0].carspeed)

    # 移动车
    for car in cars:

        car.move()

        # 碰撞且无多一条命，游戏结束
        if player.distance(car) < 20 and scoreboard.times == 1:

            print("Collison, Died!")

            game_is_on = False

            scoreboard.gameover()

            screen.exitonclick()

        # 碰撞，但生命值还有剩余
        elif player.distance(car) < 20 and scoreboard.times > 1:

            print("Collison, times minus 1!")

            player.restart()

            scoreboard.lifeminus()

    # 过关
    if player.ycor() >= 120:

        player.restart()

        # 升级
        scoreboard.levelup()

        # 车速加快
        carspeednow *= 0.8

    # 左越界处理
    if player.xcor() < -130:

        #print("Finally!")

        player.right()

    # 右越界处理
    if player.xcor() > 130:

        player.left()


        #print(cars[0].carspeed)

        #screen.exitonclick()

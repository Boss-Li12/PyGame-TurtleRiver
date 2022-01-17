#scoreboard.py

from turtle import Turtle

# 字体大小
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()

        self.penup()

        self.hideturtle()

        self.color("Black")

        # 当前等级
        self.level = 1

        # 当前生命值
        self.times = 3

        # 当前得分
        self.score = 0

        self.update_level()

        self.update_times()

        self.update_score()

    # 更新得分
    def update_score(self):

        self.goto(0,120)

        self.write(f"分数:{self.score} ", align='Center', font = FONT)

    # 更新等级
    def update_level(self):

        self.goto(-100,120)

        self.write(f"等级:{self.level} ", align='Center', font = FONT)

    # 更新生命值
    def update_times(self):

        self.goto(100, 120)

        self.write(f"生命值:{self.times} ", align='Center', font = FONT)

    # 游戏结束显示
    def gameover(self):

        self.goto(0,0)

        self.write("GAME OVER", align='Center', font=FONT)

    # 升级处理
    def levelup(self):

        self.level += 1

        self.score += 10

        self.clear()

        self.update_level()

        self.update_times()

        self.update_score()

    # 生命值减小处理
    def lifeminus(self):

        self.times -= 1

        self.clear()

        self.update_level()

        self.update_times()

        self.update_score()

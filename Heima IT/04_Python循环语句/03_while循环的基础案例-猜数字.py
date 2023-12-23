"""
演示while循环的基础案例-猜数字
"""
# 获取范围在1-100的随机数字
import random
num = random.randint(1, 100)
# 定义一个变量，记录总共猜了多少次
count = 0

flag = True
while flag:
    guess_num = int(input("猜猜数字："))
    count += 1
    if guess_num == num:
        print("猜对了")
        flag = False
    else:
        if guess_num > num:
            print("没猜对，大了")
        else:
            print("没猜对，小了")
print(f"你总共猜测了{count}次。")

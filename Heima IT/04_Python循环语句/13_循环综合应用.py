"""
循环综合应用练习-发工资
"""
import random
# 账号有1万余额
money = 10000
for member in range(1, 21):
    level = random.randint(1, 10)
    if level >= 5:
        money = money - 1000
        print(f"向员工{member}发放工资1000元，账户余额还剩{money}元。")
    else:
        print(f"员工{member}，绩效分{level}，低于5，不发工资，下一位。")
    if money <= 0:
        print("工资发完了，下个月领取吧")
        break

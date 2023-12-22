"""
演示判断语句的实战案例：终极猜数字
"""
# 构建一个随机的数字变量
import random
num = random.randint(1, 10)
# 接收输入的数字
guess_num = int(input("1到10之间猜猜数字："))

# 第一次猜测
if guess_num != num:
    if guess_num > num:
        print("猜错了，大了")
    else:
        print("猜错了，小了")
    # 第二次猜测
    guess_num = int(input("再猜猜："))
    if guess_num != num:
        if guess_num > num:
            print("又猜错了，大了")
        else:
            print("又猜错了，小了")
        # 第三次猜测
        guess_num = int(input("最后再猜猜："))
        if guess_num != num:
            print(f"还是猜错了，数字是{num}")
        else:
            print("最后一次猜对啦")
    else:
        print("第二次就才对啦")
else:
    print("第一次就才对啦")

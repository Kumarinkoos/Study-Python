"""
演示练习题：成年人判断
"""
print("欢迎来到儿童游乐园，儿童免费，成人收费。")
# 通过input语句，获得键盘输入，赋值给变量age
age = int(input("请输入你的年龄："))
if age >= 18:
    print("您已成年，游玩需要补票10元")
print("祝您游玩愉快。")

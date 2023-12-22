"""
演示练习题：猜猜心里数字
"""
num = 10

if int(input("请输入第一次猜想的数字：")) == num:
    print("第一次就猜对啦。")
elif int(input("不对，再猜一次：")) == num:
    print("第二次就猜对啦。")
elif int(input("不对，再猜最后一次：")) == num:
    print("终于猜对啦。")
else:
    print(f"Sorry，全部猜错来，我想的是：{num}")

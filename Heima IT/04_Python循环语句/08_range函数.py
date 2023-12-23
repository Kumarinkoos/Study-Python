"""
演示Python中的range()函数的基本使用
"""
# range(num)
for x in range(10):
    # 从0开始到10（不包含10）
    print(x)

print("=========")

# range(num1, num2)
for x in range(5, 10):
    # 从5开始到10（不包含10）
    print(x)

print("=========")

# range(num1, num2, step)
for x in range(5, 10, 2):
    # 从5开始到10（不包含10），步长为2
    print(x)


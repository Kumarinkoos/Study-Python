"""
演示使用while的嵌套循环
打印输出九九乘法表
"""
i = 1
j = 1
# 外层控制行
while i < 10:
    # 内层控制列
    while j <= i:
        print(f"{j}*{i}={j * i}", end="\t")
        j += 1
    print()
    j = 1
    i += 1

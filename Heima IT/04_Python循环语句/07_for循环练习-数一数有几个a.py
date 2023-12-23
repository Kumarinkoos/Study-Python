"""
演示练习-数一数有几个a
"""

name = "itheima is brand of itcast"
count = 0
for x in name:
    if x == "a":
        count += 1
print(f"上述的字符串有{count}个a")
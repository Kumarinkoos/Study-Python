"""
演示对序列进行切片操作
"""
# 对list进行切片，从1开始，4结束，步长为1
my_list = [0, 1, 2, 3, 4, 5, 6]
result = my_list[1: 4]
print(f"结果1为：{result}")

# 对tuple进行切片，从头开始，到最后结束，步长为1
my_tuple = (0, 1, 2, 3, 4, 5, 6)
result = my_tuple[:]
print(f"结果2为：{result}")

# 对string进行切片，从头开始，到最后结束，步长为2
my_str = "01234567"
result = my_str[::2]
print(f"结果3为：{result}")

# 对string切片，从头开始，到最后结束，步长为-1
my_str = "01234567"
result = my_str[::-1]
print(f"结果4为：{result}")

# 对list进行切片，从3开始，到1结束，步长为-1
my_list = [0, 1, 2, 3, 4, 5, 6]
result = my_list[3: 1: -1]
print(f"结果5为：{result}")

# 对tuple进行切片，从头开始，到尾结束，步长为-2
my_tuple = (0, 1, 2, 3, 4, 5, 6)
result = my_tuple[::-2]
print(f"结果6为：{result}")

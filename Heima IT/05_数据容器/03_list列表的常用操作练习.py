"""
演示list常用操作的练习题
"""
# 定义一个列表
num_list = [21, 25, 21, 23, 22, 20]
print(f"初始的列表为{num_list}")

# 追加一个数字到列表尾部
num_list.append(31)
print(f"在尾部追加一个元素后的列表为{num_list}")

# 追加一个新列表到尾部
new_num_list = [29, 33, 30]
num_list.extend(new_num_list)
print(f"被追加的列表为{new_num_list}")
print(f"原列表追加一个新列表后为{num_list}")

# 取出第一个元素
element_first = num_list.pop(0)
print(f"取出的第一个元素是{element_first}")
print(f"取出第一个元素后的列表为{num_list}")

# 取出最后一个元素
element_last = num_list.pop(-1)
print(f"取出的最后一个元素是{element_last}")
print(f"取出最后一个元素后的列表为{num_list}")

# 查找元素在列表中的下标位置
index = num_list.index(31)
print(f"数字31在列表的下标为{index}")

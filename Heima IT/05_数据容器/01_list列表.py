"""
演示数据容器之：list列表
语法：[元素, 元素, ....]
"""
# 定义一个列表list
code_language = ["C", "C++", "Java", "Python"]
print(code_language)
print(type(code_language))

my_list = ["Python", 111, True]
print(my_list)
print(type(my_list))

# 定义一个嵌套列表
my_list = [[1, 2, 3], [4, 5, 6]]
print(my_list)
print(type(my_list))

# 通过下标索引取出对应位置的数据
code_language = ["C", "C++", "Java", "Python"]
print(code_language[0])
print(code_language[1])
print(code_language[2])
print(code_language[3])

# 通过下标索引取出数据（倒叙取出）
print(code_language[-1])
print(code_language[-2])
print(code_language[-3])
print(code_language[-4])

# 取出嵌套列表的元素
my_list = [[1, 2, 3], [4, 5, 6]]
print(my_list[0][1])

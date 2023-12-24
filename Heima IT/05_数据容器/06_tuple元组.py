"""
演示tuple元组的定义和操作
"""
# 定义元组
t1 = ("C", "C++", "Java", "Python")
t2 = ()
t3 = tuple()
print(f"t1的类型是{type(t1)}，内容是{t1}")
print(f"t2的类型是{type(t2)}，内容是{t2}")
print(f"t3的类型是{type(t3)}，内容是{t3}")

# 定义单个元素的元组，元素后面要有逗号，不然就是字符串了
t4 = ("hello",)
print(f"t4的类型是{type(t4)}，内容是{t4}")

# 元组的嵌套
t5 = ((1, 2, 3), (4, 5, 6))
print(f"t5的类型是{type(t5)}，内容是{t5}")

element = t5[1][2]
print(f"从嵌套元组中取出的数据是：{element}")

code_language = ("C", "C++", "Java", "Python")
# 元组的的操作：index查找方法
index = code_language.index("Python")
print(f"在元组中查找Python的下标是：{index}")

# 元组的操作：count统计方法
num = code_language.count("C")
print(f"在元组中C的个数有：{num}")

# 元组的操作：len函数统计元组元素数量
length = len(code_language)
print(f"元组有{length}个元素")

# 元组的遍历：while
index = 0
while index < len(code_language):
    print(f"元组的元素为：{code_language[index]}")
    index += 1

# 元组的遍历：for
for element in code_language:
    print(f"元组的元素：{element}")

# 元组不能修改但元组里的列表里的元组可以修改
new_code_language = (["C", "C++", "Java", "Python"], ["JavaScript", "Node", "JSON"])
print(f"新元组的内容是{new_code_language}")
new_code_language[0][1] = "C#"
new_code_language[1][0] = "PHP"
print(f"新元组的列表内容修改后的内容是{new_code_language}")


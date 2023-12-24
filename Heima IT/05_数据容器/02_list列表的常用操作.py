"""
演示数据容器之：list列表的常用操作
"""
code_language = ["C", "C++", "Java", "Python"]
# 1.1 查找某元素在列表内的下标索引
index = code_language.index("Python")
print(f"Python在列表中的下标索引值是{index}")

# 1.2 如果被查找的元素不存在，会报错
# index = code_language.index("C#")
# print(f"C#在列表中的下标索引值是{index}")

# 2 修改特定下标索引的值
code_language[1] = "C#"
print(f"列表被修改后为{code_language}")

# 3 在指定下标位置插入新元素
code_language.insert(1, "C++")
print(f"插入元素后的列表为{code_language}")

# 4 在列表的尾部追加单个新元素
code_language.append("PHP")
print(f"尾部追加一个元素后的列表为{code_language}")

# 5 在列表的尾部追加一批新元素
new_code_language = ["JavaScript", "Node", "JSON"]
code_language.extend(new_code_language)
print(f"尾部追加了一批元素后的列表为{code_language}")

# 6 删除指定下标索引的元素（2种方式）
# 6.1 方式1：del 列表[下标]
del code_language[2]
print(f"列表删除元素后为{code_language}")

# 6.2 方式2：列表.pop(下标)
element = code_language.pop(2)
print(f"通过pop得到的元素为{element}")
print(f"通过pop取出元素后的列表为{code_language}")

# 7 删除某元素在列表中的第一个匹配项
code_language.remove("Node")
print(f"通过remove移除元素后的列表为{code_language}")

# 8 清空列表
code_language.clear()
print(f"列表清空后为{code_language}")

# 9 统计列表内某元素的数量
code_language = ['C', 'C++', 'C#', 'Java', 'Python', 'PHP', 'JavaScript', 'Node', 'JSON']
count = code_language.count("Python")
print(f"列表中Python的数量有{count}")

# 10 统计列表中全部的元素数量
num = len(code_language)
print(f"这个列表总共有{num}个元素")

"""
演示数据容器集合的使用
"""
# 定义集合
code_set = {"Java", "C", "Python", "C++", "Python", "Java"}
my_set = set()
print(f"集合的内容是{code_set}，类型是{type(code_set)}")
print(f"空集合的内容是{my_set}，类型是{type(my_set)}")

# 添加新元素
code_set.add("PHP")
code_set.add("Python")
print(f"集合添加元素后为{code_set}")

# 移除元素
code_set.remove("Java")
print(f"集合移除元素后为{code_set}")

# 随机取出一个元素
element = code_set.pop()
print(f"被取出的元素为{element}，取出后的集合为{code_set}")

# 清空集合
code_set.clear()
print(f"被清空后的集合为{code_set}")

# 取2个集合的差集
code_set1 = {"Java", "Python", "PHP"}
code_set2 = {"Java", "Python", "C++"}
code_diff_set1 = code_set1.difference(code_set2)
code_diff_set2 = code_set2.difference(code_set1)
print(f"set1的结果为{code_set1}")
print(f"set2的结果为{code_set2}")
print(f"set3的结果为{code_diff_set1}")
print(f"set4的结果为{code_diff_set2}")

# 消除2个集合的差集
code_set1.difference_update(code_set2)
print(f"集合1的结果为{code_set1}")
print(f"集合2的结果为{code_set2}")

# 2个集合合并为1个
code_set1 = {"Java", "Python", "PHP"}
code_set2 = {"Java", "Python", "C++"}
code_union_set = code_set1.union(code_set2)
print(f"集合1的结果为{code_set1}")
print(f"集合2的结果为{code_set2}")
print(f"集合后的集合3的结果为{code_union_set}")

# 统计集合元素数量
num = len(code_union_set)
print(f"最终的集合的元素有{num}个")

# 集合的遍历，集合无法用下标索引所以无法用while循环
for element in code_union_set:
    print(f"取出的元素有：{element}")

"""
set集合练习：信息去重
"""
code_list = ["Python", "Java", "C", "Python", "Java", "PHP"]
code_set = set()
# 遍历list添加到set里
for element in code_list:
    code_set.add(element)
print(f"去重后的信息为{code_set}")

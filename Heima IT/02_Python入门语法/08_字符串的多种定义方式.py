"""
演示字符串的三种定义方式：
- 单引号定义法
- 双引号定义法
- 三引号定义法
"""

# 单引号定义法，使用单引号进行包围
name = 'Python'
print(type(name))

# 双引号定义法
name2 = "Java"
print(type(name2))

# 三引号定义法，写法和多行注释是一样的
name3 = """
C
C++
Java
Python
"""
print(type(name3))
print(name3)

# 在字符串内包含双引号
name = 'Python "Wang"'
print(name)
# 在字符串内包含单引号
name = "Python 'Wang'"
print(name)
# 使用转义字符\解除引号效用
name = "Python \"Wang\""
print(name)

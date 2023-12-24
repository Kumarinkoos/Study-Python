"""
演示以数据容器的角色，学习字符串的相关操作
"""
code_string = "Python and Java"
# 通过下标索引取值
value = code_string[2]
value2 = code_string[-3]
print(f"字符串的第三位是{value}")
print(f"字符串的倒数第三位是{value2}")

# index方法
num = code_string.index("and")
print(f"在字符串中and的首字母的下标是{num}")

# replace方法
new_code_string = code_string.replace("Java", "PHP")
print(f"将字符串{code_string}进行替换后得到{new_code_string}")

# split方法
code_list = code_string.split(" ")
print(f"字符串{code_string}进行切割后得到列表{code_list}")

# strip方法
code_string = "  Python and Java  "
new_code_string = code_string.strip()   # 去除首位空格
print(f"字符串{code_string}经过strip后得到{new_code_string}")

code_string = "12Python and Java21"
new_code_string = code_string.strip("12")   # 去除字符1和字符2
print(f"字符串{code_string}去除掉1和2后得到{new_code_string}")

# 统计字符串中某字符串的出现次数
num = code_string.count("1")
print(f"字符串中的字符1出现的次数有{num}次")

# 统计字符串的长度
length = len(code_string)
print(f"字符串的长度为{length}")

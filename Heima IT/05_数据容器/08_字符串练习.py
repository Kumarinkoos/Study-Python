"""
字符串练习：分割字符串
"""
my_str = "itheima itcast boxuegu"
# 统计字符串内有多少个"it"
count_str = my_str.count("it")
print(f"字符串中有{count_str}个'it'")

# 用｜替换空格
new_my_str = my_str.replace(" ", "|")
print(f"字符串被替换后为{new_my_str}")

# 以｜进行字符串的分割，得到列表
my_str_list = new_my_str.split("|")
print(f"字符串{new_my_str}进行切割后得到的列表为{my_str_list}")

"""
演示字典的操作
"""
score_dict = {"Wang": 99, "Hong": 90, "Yao": 85}
# 新增元素
print(f"初始字典为{score_dict}")
score_dict["Ye"] = 66
print(f"添加元素后为{score_dict}")

# 更新元素
score_dict["Wang"] = 88
print(f"更新元素后为{score_dict}")

# 删除元素
element = score_dict.pop("Wang")
print(f"删除元素的字典为{score_dict}，删除的值为{element}")

# 清空元素
score_dict.clear()
print(f"清空后的字典为{score_dict}")

# 获取全部的key
score_dict = {"Wang": 99, "Hong": 90, "Yao": 85}
keys = score_dict.keys()
print(f"字典的所有的key是{keys}，类型是{type(keys)}")

# 遍历字典
# 方式1
for key in keys:
    element = score_dict[key]
    print(f"{key}的成绩是{element}")

# 方式2
for key in score_dict:
    element = score_dict[key]
    print(f"方式2：{key}的成绩是{element}")

# 统计字典内的元素数量
length = len(score_dict)
print(f"字典的元素数量有{length}个")

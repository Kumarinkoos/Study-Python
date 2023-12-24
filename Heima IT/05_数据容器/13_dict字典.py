"""
演示数据容器字典
"""
# 定义字典
score_dict = {"Wang": 99, "Hong": 90, "Yao": 85}

# 定义空字典
empty_dict1 = {}
empty_dict2 = dict()
print(f"字典1的内容为{score_dict}，类型为{type(score_dict)}")
print(f"字典2的内容为{empty_dict1}，类型为{type(empty_dict1)}")
print(f"字典3的内容为{empty_dict2}，类型为{type(empty_dict2)}")

# 从字典中给予Key获取Value
wang_score = score_dict["Wang"]
print(f"wang的分数是{wang_score}")
hong_score = score_dict["Hong"]
print(f"hong的分数是{hong_score}")
yao_score = score_dict["Yao"]
print(f"yao的分数是{yao_score}")

# 定义嵌套字典
score_dict = {
    "Wang": {"语文": 77, "数学": 66, "英语": 33},
    "Hong": {"语文": 88, "数学": 86, "英语": 55},
    "Yao": {"语文": 99, "数学": 96, "英语": 66}
}
print(f"学生的成绩信息是{score_dict}")

# 从嵌套字典中获取数据
Wang_Yu_score = score_dict["Wang"]["语文"]
print(f"Wang的语文成绩是{Wang_Yu_score}")

"""
使用一个字典来存储一些人喜欢的数字。请想出5个人的名字，
并将这些名字用作字典中的键；想出每个人喜欢的一个数字，
并将这些数字作为值存储在在店中。打印每个人的名字和喜欢的数字。
"""
favorite_number = {
    "Wang": 17,
    "Chen": 14,
    "Hong": 66,
    "Yao": 7,
    "Ye": 8
}
print(f"Wang喜欢的数字是{favorite_number['Wang']}")
print(f"Chen喜欢的数字是{favorite_number['Chen']}")
print(f"Hong喜欢的数字是{favorite_number['Hong']}")
print(f"Yao喜欢的数字是{favorite_number['Yao']}")
print(f"Ye喜欢的数字是{favorite_number['Ye']}")

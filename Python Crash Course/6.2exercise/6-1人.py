"""
使用一个字典来存储一个熟人信息，包括名、姓、年龄和居住城市。
该字典应包含键 first_name、last_name、age和city。
将存储在该字典中的每项信息都打印出来。
"""
friend_dict = {
    "first_name": "Yao",
    "last_name": "Ye",
    "age": 27,
    "city": "Ning Bo"
}
print(f"我的朋友名字叫{friend_dict['first_name']}"
      f"{friend_dict['last_name']}，"
      f"他的年龄有{friend_dict['age']}岁，"
      f"他住在{friend_dict['city']}。")

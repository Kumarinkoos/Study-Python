"""
dict字典练习：升职加薪
"""
member_dict = {
    "Wang": {"部门": "科技部", "工资": 3000, "级别": 1},
    "Hong": {"部门": "市场部", "工资": 5000, "级别": 2},
    "Yao": {"部门": "市场部", "工资": 7000, "级别": 3},
    "Chen": {"部门": "科技部", "工资": 4000, "级别": 1},
    "Fei": {"部门": "市场部", "工资": 6000, "级别": 2},
}
# 显示原本的信息
for name in member_dict:
    print(f"目前的信息状况为：{name}: {member_dict[name]}")

# 遍历加薪
for name in member_dict:
    if member_dict[name]["级别"] == 1:
        member_dict[name]["级别"] = 2
        member_dict[name]["工资"] = member_dict[name]["工资"] + 1000

# 显示加薪后的信息
for name in member_dict:
    print(f"加薪后的信息状况为：{name}: {member_dict[name]}")

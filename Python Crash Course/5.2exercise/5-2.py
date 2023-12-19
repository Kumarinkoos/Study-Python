users = ["Wang", "Chen"]
user = "Wang"
age = 27
# 检查两个字符串相等
if user == "wang":
    print("yes")
else:
    print("no")
# 检查两个字符串不等
if user != "wang":
    print("yes")
else:
    print("no")
# 使用lower测试
if user.lower() == "wang":
    print("yes")
else:
    print("no")
# 检查两个数相等
if age == 27:
    print("yes")
else:
    print("no")
# 检查两个数不等
if age != 27:
    print("yes")
else:
    print("no")
# 检查大于
if age > 27:
    print("yes")
else:
    print("no")
# 检查小于
if age < 27:
    print("yes")
else:
    print("no")
# 检查大于等于
if age >= 27:
    print("yes")
else:
    print("no")
# 检查小于等于
if age <= 27:
    print("yes")
else:
    print("no")
# 使用and
if (age > 18) and (age < 30):
    print("yes")
else:
    print("no")
# 使用or
if (age > 18) or (age < 30):
    print("yes")
else:
    print("no")
# 使用in
if user in users:
    print("yes")
else:
    print("no")
# 使用not in
if user not in users:
    print("yes")
else:
    print("no")

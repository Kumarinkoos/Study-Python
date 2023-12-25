alien_0 = {"color": "green", "points": 5}

# 访问字典中的值
new_point = alien_0["points"]
print("You just earned " + str(new_point) + " points!")

# 添加键值对
print(alien_0)

alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

# 创建空的字典
alien_0 = {}
print(alien_0)

alien_0["color"] = "green"
alien_0["points"] = 5
print(alien_0)

# 修改字典中的值
print("The alien is " + alien_0["color"] + ".")
alien_0["color"] = "yellow"
print("The alien is now " + alien_0["color"] + ".")

# 删除键值对
del alien_0["points"]
print(alien_0)

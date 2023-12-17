players = ["charles", "martina", "micheal", "florence", "eli", "Yao", "Ye", "Wang"]

# 打印前三个元素
print("The first three items in the list are:")
for player in players[:3]:
    print(player.title())

# 打印中间三个元素
print("Three items from the middle of the list are:")
for player in players[2:5]:
    print(player.title())

# 打印末尾三个元素
print("The last three items in the list are:")
for player in players[-3:]:
    print(player.title())

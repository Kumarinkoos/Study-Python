players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0: 3])
print(players[1: 4])
# 如果没有指定第一个索引，Python将自动从列表开头开始。
print(players[: 4])
# 如果没有指定终止的索引，Python将切片于列表末尾
print(players[2:])
# 可以用负数索引来进行切片
print(players[-3:])

# 如果要遍历列表的部分元素，可在for循环中使用切片
print("Here are the first three players on my team:")
for players in players[-3:]:
    print(players.title())

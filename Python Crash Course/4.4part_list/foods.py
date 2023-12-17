my_foods = ["pizza", "falafel", "carrot cake"]
# 复制一个列表
friend_foods = my_foods[:]
# 这只是把列表的地址赋值给另一个变量来
your_foods = my_foods

my_foods.append("cannoli")
friend_foods.append("ice cream")
your_foods.append("noodles")

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("\nYou favorite foods are:")
print(your_foods)

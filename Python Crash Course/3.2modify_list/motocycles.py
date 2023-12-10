motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

# 修改列表元素
motorcycles[0] = "ducati"
print(motorcycles)

# 添加列表元素
print("========================")
# 在列表末尾添加元素
motorcycles[0] = "honda"
motorcycles.append("ducati")
print(motorcycles)

# 在列表中插入元素
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.insert(0, "ducati")
print(motorcycles)

# 删除列表元素
print("========================")
# 使用del删除元素
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
del motorcycles[0]
print(motorcycles)

# 使用pop弹出元素（从列表中删除并接着使用它的值）
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
print("The last motorcycles I owned was a " + popped_motorcycles.title() + ".")
# 弹出列表中任何位置的元素
motorcycles = ["honda", "yamaha", "suzuki"]
first_owned = motorcycles.pop(0)
print("The first motorcycles I owned was a " + first_owned.title() + ".")

# 根据值删除元素
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)
motorcycles.remove("ducati")
print(motorcycles)

motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

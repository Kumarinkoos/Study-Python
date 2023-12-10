# 使用sort()对列表进行永久性排序
cars = ["bwm", "audi", "toyota", "subaru"]
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

print("=============")
# 使用sorted()对列表进行临时排序
cars = ["bwm", "audi", "toyota", "subaru"]
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list:")
print(cars)

print("============")
# 反转列表元素对排序顺序
cars = ["bwm", "audi", "toyota", "subaru"]
print(cars)
cars.reverse()
print(cars)

print("============")
# 确定列表对长度
cars = ["bwm", "audi", "toyota", "subaru"]
print(cars)
print(len(cars))

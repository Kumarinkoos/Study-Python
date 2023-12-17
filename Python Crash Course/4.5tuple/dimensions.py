# 定义元组
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# 元组是不能被修改元素的
# dimensions[0] = 250

# 遍历元组
for dimension in dimensions:
    print(dimension)

# 虽然不能修改元组的元组，但可以给存储元组的变量直接重新赋值
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

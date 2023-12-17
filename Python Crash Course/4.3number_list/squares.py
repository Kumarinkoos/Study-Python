# 用range()函数创建一个1到10到平方到数字列表
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# 代码简洁
squares = []
for value in range(1, 12):
    squares.append(value ** 2)
print(squares)

# 列表解析
squares = [number ** 2 for number in range(1, 13)]
print(squares)

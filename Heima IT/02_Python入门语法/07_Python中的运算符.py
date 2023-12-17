"""
演示Python中的各类运算符
"""
# 算术运算符
print("1 + 1 = ", 1 + 1)
print("2 - 1 = ", 2 - 1)
print("3 * 3 = ", 3 * 3)
print("4 / 2 = ", 4 / 2)
print("11 + 2 = ", 11 // 2)
print("9 % 2 = ", 9 % 2)

# 赋值运算符
num = 1 + 2 * 3
# 复合赋值运算符
num2 = 1
num2 += 1   # num = num + 1
print("num2 += 1：", num2)
num2 -= 1
print("num2 -= 1：", num2)
num2 *= 5
print("num2 *= 5：", num2)
num2 /= 2
print("num2 /= 2：", num2)
num3 = 3
num3 %= 2
print("num3 %= 3：", num3)
num3 **= 2
print("num3 **= 2：", num3)
num3 //= 2
print("num3 //= 2：", num3)

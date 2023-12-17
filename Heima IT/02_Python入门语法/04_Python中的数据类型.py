# 方式1：使用print直接输出类型信息
print(type("Python"))
print(type(11))
print(type(3.14))

# 方式2：使用变量存储type()语句的结果
string_type = type("Python")
int_type = type(11)
float_type = type(3.14)
print(string_type)
print(int_type)
print(float_type)

# 方式3：使用type()语句，查看变量中存储的数据类型信息
name = "Python"
name_type = type(name)
print(name_type)

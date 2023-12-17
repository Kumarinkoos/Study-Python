# 通过占位的形式，完成拼接
name = "Python"
message = "Hello %s" % name
print(message)

# 通过占位的形式，完成数字和字符串的拼接
class_num = 57
avg_salary = 16781
message = "班级：%s，工资：%s" % (class_num, avg_salary)
print(message)

name = "科大讯飞"
setup_year = 2006
stock_price = 50.46
message = "%s，成立于%d，今天的股价是%f" % (name, setup_year, stock_price)
print(message)

num1 = 11
num2 = 11.345
print("数字11宽度限制5，结果是：%5d" % num1)
print("数字11宽度限制1，结果是：%1d" % num1)
print("数字11.345宽度限制7，小数精度2，结果是：%7.2f" % num2)
print("数字11.345宽度不限制，小数精度2，结果是：%.2f" % num2)

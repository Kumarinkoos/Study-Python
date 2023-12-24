"""
序列的切片练习
"""
# 得到Python
code = "avaJ,nohtyPdna++C,#C"
print(code)
# 切片
code1 = code[10: 4: -1]
print(code1)

# split方法
code2 = code.split(",")
print(code2)
need_code = code2[1][5::-1]
print(need_code)

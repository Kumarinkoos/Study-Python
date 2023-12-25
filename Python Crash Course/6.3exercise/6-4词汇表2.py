"""
整理6-3，将其中的中的一系列print语句替换为一个遍历字典中的键值循环。
确定循环正确无误后，再在词汇表中添加5个Python属于。当再次运行这个程序时，
这些新术语及其含义将自动包含在输出中。
"""
python_word = {
    "list": "列表",
    "tuple": "元组",
    "set": "集合",
    "string": "字符串",
    "dictionary": "字典"
}
print(python_word)
python_word["import"] = "导入"
python_word["class"] = "类"
python_word["del"] = "删除"
python_word["break"] = "中断"
python_word["for"] = "循环"
print(python_word)

for key in python_word.keys():
    print(f"{key}: \n\t{python_word[key]}")

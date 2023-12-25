"""
Python字典可用于模拟现实生活中的字典，但为避免混淆，
我们将后者称之为词汇表。
- 想出在前面学过的5个编程词汇，将它们用作词汇表中的键，
  并将它们的含义作为值存储在词汇表中。
- 以整洁的方式打印每个词汇及其含义。为此，可以先打印词汇，
  在它后面加上一个冒号，再打印词汇的含义；也可以一行打印词汇，
  再使用换行符（\n）插入一个空行，然后在一行以缩进的方式打印词汇的含义。
"""
program_word = {
    "list": "列表",
    "tuple": "元组",
    "set": "集合",
    "string": "字符串",
    "dictionary": "字典"
}
print(f"list：\n\t{program_word['list']}")
print(f"tuple：\n\t{program_word['tuple']}")
print(f"set：\n\t{program_word['set']}")
print(f"string：\n\t{program_word['string']}")
print(f"dictionary：\n\t{program_word['dictionary']}")

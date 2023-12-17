# 用for循环来遍历列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    # for循环可对每个元素执行任何操作
    print(magician.title() + ", that was a great trick!")
    # for循环再添加一行循环代码
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
# 没有缩进就结束循环
print("Thank you, everyone. That was a great magic show!")
# 下面这个会报warning，不会报error
# print(magician.title())

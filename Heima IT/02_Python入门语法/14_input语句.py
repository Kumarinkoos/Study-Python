"""
演示Python的input语句
获取键盘的输入信息
"""
print("请告诉我你是谁？")
name = input()
print("我知道了，你是：%s" % name)

name = input("请告诉我我是谁？")
print("原来如此，我是%s" % name)

# 输入数字类型
num = input("请告诉我银行卡密码")
print("你的银行卡密码类型是：", type(num))
int_num = int(num)
print("现在是：", type(int_num))

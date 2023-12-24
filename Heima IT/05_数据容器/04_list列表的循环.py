"""
演示对list列表的循环，使用while和for循环2种方式
"""


def list_while_func():
    """
    使用while循环遍历列表的演示函数
    :return: None
    """
    code_language = ["C", "C++", "Java", "Python"]
    # 定义一个变量来标记列表的下标
    index = 0
    while index < len(code_language):
        # 通过index来取出对应下标的元素
        element = code_language[index]
        print(f"列表的元素：{element}")
        # 将循环变量+1
        index += 1


def list_for_func():
    """
    使用for循环遍历列表的演示函数
    :return: None
    """
    code_language = ["C", "C++", "Java", "Python"]
    for element in code_language:
        print(f"列表的元素为：{element}")


list_while_func()
list_for_func()

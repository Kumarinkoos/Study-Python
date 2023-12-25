"""
在完成练习6-1的程序中，再创建两个表示人的字典，然后将这三个字典都存储在一个名为people的列表中。
遍历这个列表，将其中每个人的所有信息都打印出来。
"""
wang = {'first': 'Wang', 'last': 'Chen', 'location': 'China'}
hong = {'first': 'Hong', 'last': 'Fei', 'location': 'China'}
yao = {'first': 'Yao', 'last': 'Ye', 'location': 'China'}

friends = [wang, hong, yao]

for friend in friends:
    print(f"{friend['first']} {friend['last']} is from {friend['location']}")

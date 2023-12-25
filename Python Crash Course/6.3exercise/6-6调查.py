"""
在favorite_languages中执行以下操作
- 创建一个应该会接受调查的人员名单，其中有些人已包含在字典中，而其他人未包含在字典中。
-  遍历这个人员名单，对于已参与调查的人，打印一条消息表示感谢。
   对于还未参与调查的人，打印一条消息邀请他参与调查。
"""
favorite_languages = {
    'jen': 'Python',
    'sarah': 'C',
    'edward': 'Ruby',
    'phil': 'Python'
}

member_list = ['jen', 'sarah', 'edward', 'phil', 'wang', 'yao', 'hong', 'ye']

for member in member_list:
    if member in favorite_languages.keys():
        print(f"感谢{member}参与调查")
    else:
        print(f"邀请{member}参加调查")

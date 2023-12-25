"""
修改6-2点程序，让每个人都可以有多个喜欢的数字，然后将每个人的名字及其喜欢的数字打印出来。
"""
favorite_number = {
    'wang': [16, 17],
    'hong': [6, 8],
    'yao': [233, 311]
}

for name, numbers in favorite_number.items():
    print(f"\n{name}")
    for number in numbers:
        print(f"\t{number}")

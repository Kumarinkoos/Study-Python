"""
创建一个名为favorite_places的字典。在这个字典中，将三个人的名字用作键；
对于其中的每个人，都存储他喜欢的1～3个地方。
"""
favorite_places = {
    'wang': ['ZheJiang'],
    'hong': ['GuangXi', 'TianJin'],
    'yao': ['ZheJiang', 'BeiJing']
}

for name, places in favorite_places.items():
    print(f"\n{name}:")
    for place in places:
        print(f"\t{place}")

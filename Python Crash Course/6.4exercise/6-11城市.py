"""
创建一个名为cities的字典，其中将三个城市名用作键；
对于每座城市，都创建一个字典，并在其中包含该城市所属的国家、人口约数以及一个有关该城市的事实。
在表示每座城市的字典中，应包含country、population和fact等键。
将每座城市的名字以及有关它们的信息都打印出来。
"""
cities = {
    'NingBo': {'country': 'China', 'population': '100万', 'fact': 'see'},
    'GuiLing': {'country': 'China', 'population': '60万', 'fact': 'mountain'},
    'BeiJing': {'country': 'China', 'population': '200', 'fact': 'capital'}
}

for city, city_info in cities.items():
    print(f"\n{city}: ")
    print(f"\tcountry is {city_info['country']}")
    print(f"\tpopulation is {city_info['population']}")
    print(f"\tfact is {city_info['fact']}")

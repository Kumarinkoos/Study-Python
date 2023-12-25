"""
创建一个字典，在其中存储三条大河流及其流经的国家。其中一个键值对
可能是'nile':'egypt'
- 使用循环为每条河流打印一条信息。
- 使用循环将该字典中每条河流的名字都打印出来。
- 使用循环将该字典包含的每个国家的名字都打印出来。
"""
river_dict = {
    "HuangHe": "China",
    "Nile": "Egypt",
    "Chang Jiang": "China"
}

for river, country in river_dict.items():
    print(f"The {river} runs through {country}.")

for river in river_dict.keys():
    print(river)

for country in river_dict.values():
    print(country)

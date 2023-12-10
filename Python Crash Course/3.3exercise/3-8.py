place = ["Bei Jing", "Shang Hai", "Osaka", "Kyoto", "Tokyo"]
print(place)
# 使用sorted()按顺序打印这个列表，同时不修改它
sorted_place = sorted(place)
print(sorted_place)
print(place)
sorted2_place = sorted(place, reverse=True)
print(sorted2_place)
print(place)
# 使用reverse()改变元素排列顺序
place.reverse()
print(place)
place.reverse()
print(place)
# 使用sort()改变列表使其元素排序
place.sort()
print(place)
place.sort(reverse=True)
print(place)

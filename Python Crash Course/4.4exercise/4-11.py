pizzas = ["烤肉披萨", "原味披萨", "芝士披萨"]
friend_pizzas = pizzas[:]
pizzas.append("香肠披萨")
friend_pizzas.append("五花肉披萨")
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

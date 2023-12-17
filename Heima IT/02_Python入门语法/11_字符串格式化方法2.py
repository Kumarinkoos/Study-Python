"""
演示第二种字符串格式化的方式：f{占位}
"""
name = "科大讯飞"
setup_year = 2006
stock_price = 50.46
message = f"{name}，成立于{setup_year}，今天的股价是{stock_price}"
print(message)

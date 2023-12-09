# 使用方法修改字符串的大小写
name = "ada lovelace"
print(name.title())

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# 合并（拼接）字符串
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

print("Hello, " + full_name.title() + "!")

message = "Hello, " + full_name + "!"
print(message)

# 使用制表符或换行符来添加空白
print("Python")
print("\tPython")

print("Languages:\nPython\nC\nJavaScript")

print("Languages:\n\tPython\n\tC\n\tJavaScript")

# 删除空白
favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language)

favorite_language = favorite_language.rstrip()
print(favorite_language)

favorite_language = " python "
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

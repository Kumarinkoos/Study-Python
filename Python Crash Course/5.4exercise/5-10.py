current_users = ["admin", "Eric", "Mike", "Wang", "Chen"]
new_users = ["eric", "wang", "Yao", "ye"]
current_users_lower = []

for current_user in current_users:
    current_users_lower.append(current_user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user}需要输入别的用户名")
    else:
        print(f"{new_user}这个用户名未被使用")

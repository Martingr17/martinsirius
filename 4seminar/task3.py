login = input("Введите логин: ")
banned = "=?*^$№@_ "
for i in login:
    if i in banned:
        print(i)
games = ["собачка", "кот"]
game = input("Введите настольную игру: ")
while game != "0":
    if game in games:
        print("Эта игра уже записана")
    else:
        games.append(game)
        print("Игра добавлена в список")
    game = input("Введите настольную игру: ")
games.sort()
print(games)
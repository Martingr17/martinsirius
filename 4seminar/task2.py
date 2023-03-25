fun = input("Введите развлечение: ")
attempt = 3
if fun == "game":
    for number in range(3):
        number = int(input("Угадай число: "))
        attempt -= 1
        if number == 5:
            print("Вы выиграли билет на концерт!")
            break
        else:
            print("Вмвы не угадали число. Количество попыток:", attempt)
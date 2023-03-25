print("Здравствуйте, выбирите прием пищи")
meal = input("Прием пищи: ")
breakfast = "Завтрак"
lunch = "Обед"
if meal == breakfast:
    print("Могу предложить вам кашу")
elif meal == lunch:
    print("Могу предложить вам плов")
else:
    print("Могу предложить вам котлету с пюре")
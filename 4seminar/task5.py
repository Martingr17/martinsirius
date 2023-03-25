price = int(input("Введите стоимость товара: "))
while price != 0:
    discount = (int(input("Введите количество скидки в процентах: "))) / 100
    print(price - price * discount)
    price = int(input("Введите стоимость товара: "))
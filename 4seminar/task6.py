total = int(input("Введите сумму покупок: "))
discount = 0.15
while total != 0 and total % 2 == 0:
    total = total / 2
print("К оплате:", total - total * discount)
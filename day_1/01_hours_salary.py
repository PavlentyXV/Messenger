"""
Пример программы для расчета почасовой зарплаты

Данные
- пользователь вводит стоимость часа (число)
- пользователь вводит количество дней (число)

Сделать
- найти размер оплаты в руб (по кол-во дней)
- найти размер налога 13% в руб (по кол-во дней)
"""

hours_cost = int(input("Укажите стоимость часа >> "))
day_quantity = int(input("Укажите количество дней >> "))

total = (hours_cost * 8) * day_quantity
final = total - (total * .13)
print(final)
# Лабораторна робота №1. Основи Python
# Варіант: 6
# ПІБ: Довгай Владислав Володимирович

# Введення даних з перевіркою на коректність
while True:
    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
        break
    except ValueError:
        print("Помилка: введено некоректне значення. Спробуйте ще раз.")

# Обчислення суми, різниці та добутку
summa = num1 + num2
difference = num1 - num2
product = num1 * num2

# Виведення результатів
print("\nРезультати обчислень:")
print(f"Сума: {summa:.2f}")
print(f"Різниця: {difference:.2f}")
print(f"Добуток: {product:.2f}")

# Обчислення частки з перевіркою ділення на 0
if num2 != 0:
    quotient = num1 / num2
    print(f"Частка: {quotient:.2f}")
else:
    print("Частка: ділення на нуль неможливе.")

# Дод. інфо: порівняння чисел
if num1 > num2:
    print("Перше число більше за друге.")
elif num1 < num2:
    print("Перше число менше за друге.")
else:
    print("Числа рівні.")
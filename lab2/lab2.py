# Лабораторная работа №2. Введение в язык программирования Python

# ===== Задание 3: Первая программа =====
print("\n--- Задание 3 ---")
print("Hello, World!")

# ===== Задание 4: Переменные, типы данных и вывод =====
print("\n--- Задание 4 ---")
name = "Лиза"
age = 18
height = 1.65
is_student = True
print("Имя:", name)
print("Возраст:", age)
print("Рост:", height)
print("Студент:", is_student)
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
age = 19
height = 1.67
print("Возраст:", age)
print("Рост:", height)

# ===== Задание 5: Ввод данных и преобразование типов =====
print("\n--- Задание 5 ---")
first_name = input("Введите имя: ")
last_name = input("Введите фамилию: ")
age = int(input("Введите возраст: "))
height = float(input("Введите рост: "))

print(type(age))
print(age)
print(type(height))
print(height)

# ===== Задание 6: Арифметические операции =====
print("\n--- Задание 6 ---")
a = 15
b = 4

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

print((2 + 3) * 4)

# ===== Задание 7: Простой калькулятор =====
print("\n--- Задание 7 ---")
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")

# ===== Задание 8: Цикл for и функция range() =====
print("\n--- Задание 8 ---")
# числа от 1 до 10
for i in range(1, 11):
    print(i)

# числа от 10 до 1
for i in range(10, 0, -1):
    print(i)

# чётные числа от 0 до 20
for i in range(0, 21, 2):
    print(i)

# шаг 3
for i in range(0, 21, 3):
    print(i)

# ===== Задание 9: Вычисления в цикле for =====
print("\n--- Задание 9 ---")
n = int(input("Введите целое положительное число n: "))

k = 0
for i in range(1, n + 1):
    k += i

print(k)

# ===== Задание 10: Цикл while =====
print("\n--- Задание 10 ---")
count = 10

while count > 0:
    print(count)
    count -= 1

print("Цикл завершён")

# ===== Задание 11: Стандартная библиотека math =====
print("\n--- Задание 11 ---")
import math

radius = 6

print(f"Длина окружности = {2 * math.pi * radius}")
print(f"Площадь круга = {math.pi * radius ** 2}")
print(f"Квадратный корень из 16 = {math.sqrt(16)}")

# ===== Задание 12: Условные конструкции =====
print("\n--- Задание 12 ---")
number = int(input("Введите число: "))

if number > 0:
    print("Число положительное")
elif number < 0:
    print("Число отрицательное")
else:
    print("Число равно нулю")

if number % 2 == 0:
    print("Число чётное")
else:
    print("Число нечётное")

# ===== Задание 13: Логические операторы =====
print("\n--- Задание 13 ---")
age = int(input("Возраст: "))
has_access = True

print(f"Допуск имеется: {has_access}")

if age >= 18 and has_access:
    print("Доступ разрешён")
else:
    print("Доступ запрещён")

# ===== Задание 14: Самостоятельная работа: анализ измерений =====
print("\n--- Задание 14 ---")
n = int(input("Введите количество измерений: "))

total = 0

for i in range(n):
    v = float(input(f"Введите измерение {i + 1}: "))
    total += v

print(f"Сумма измерений: {total}")
print(f"Среднее арифметическое: {total / n}")

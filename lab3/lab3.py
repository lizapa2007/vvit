# Лабораторная работа №3. Функции в Python и базовые алгоритмы

# Задание 1: Создание и вызов функций
def greet(name):
    print(f"Привет, {name}")

def square(number):
    return number ** 2

def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b

greet("Иван")
greet("Мария")
print("Квадрат 5:", square(5))
print("Квадрат 12:", square(12))

print("Максимум из 3 и 7:", max_of_two(3, 7))
print("Максимум из 10 и 4:", max_of_two(10, 4))

# Задание 2: Аргументы и возвращаемые значения
def calculate_rectangle(width, height):
    return width * height


def calculate_perimeter(width, height):
    return 2 * (width + height)


def describe_rectangle(width, height, unit="cm"):
    area = calculate_rectangle(width, height)
    perimeter = calculate_perimeter(width, height)
    print(f"Прямоугольник: {width} x {height} {unit}")
    print(f"Площадь: {area} кв. {unit}")
    print(f"Периметр: {perimeter} {unit}")


describe_rectangle(6, 2)
print()
describe_rectangle(11, 9, unit="м")

# Задание 3: Области видимости переменных
value = 10


def example():
    value = 20
    local = 30
    print(value, local)


example()
print(value)

# Обращение к локальной переменной снаружи функции -> NameError
# print(local)

# Задание 4: Работа со списками
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(numbers[0])
print(numbers[2])
print(numbers[-1])


numbers[1] = 25
print(numbers)


numbers.append(111)
print(numbers)


numbers.remove(50)
print(numbers)


removed = numbers.pop()
print(removed)
print(numbers)


print(len(numbers))

# Задание 5: Срезы
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numbers[:3])
print(numbers[-3:])
print(numbers[2:7])
print(numbers[::2])
print(numbers[::-1])

# Задание 6: Работа с кортежами
measurements = (5, 4, 6, 7, 2, 8, 10, 9)

print(measurements[0])
print(measurements[-1])
print(measurements[2:6])

# Попытка изменить кортеж -> TypeError: 'tuple' object does not support item assignment
# measurements[0] = 99
# print(measurements)

first, second = measurements[:2]
print(first, second)

as_list = list(measurements)
as_list[0] = 99
new_tuple = tuple(as_list)
print(new_tuple)

# Задание 7: Встроенные функции
numbers = [5, 4, 6, 7, 2, 8, 10, 9]

print(len(numbers))
print(sum(numbers))
print(min(numbers))
print(max(numbers))

average = sum(numbers) / len(numbers)
print(average)

s = sorted(numbers)
print(numbers)
print(s)

numbers.sort()
print(numbers)

# Задание 8: Реализация собственных алгоритмов
def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def find_min(numbers):
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum


def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum


data = [5, 6, 2, 10, 4, 9, 3]

msum = calculate_sum(data)
mmin = find_min(data)
mmax = find_max(data)
print(msum, sum(data))
print(mmin, min(data))
print(mmax, max(data))

# Задание 9: Линейный поиск
def find_element(numbers, target):
    for index in range(len(numbers)):
        if numbers[index] == target:
            return index
    return -1


data = [10, 20, 30, 40, 50]

print(find_element(data, 30))
print(find_element(data, 50))
print(find_element(data, 99))

# Задание 10: Возврат нескольких значений
def analyze(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    return minimum, maximum, average


data = [5, 8, 1, 10, 6, 7, 3]

result = analyze(data)
print(result)

mn, mx, avg = analyze(data)
print(f'{mn}')
print(f'{mx}')
print(f'{avg:.2f}')

# Задание 11: Lambda-функции
numbers = [-10, 3, -2, 8, -5]

normal_sorted = sorted(numbers)
print(normal_sorted)

abs_sorted = sorted(numbers, key=lambda x: abs(x))
print(abs_sorted)

# Задание 12: Самостоятельная работа
measurements = [12, 13, 24, 55, 46, 67, 52, 87, 90, 87, 23, 18]

def calculate_average(measurements):
    total = 0
    for value in measurements:
        total += value
    return total / len(measurements)


def find_minimum(measurements):
    minimum = measurements[0]
    for value in measurements:
        if value < minimum:
            minimum = value
    return minimum


def find_maximum(measurements):
    maximum = measurements[0]
    for value in measurements:
        if value > maximum:
            maximum = value
    return maximum


def count_above_average(measurements):
    avg = calculate_average(measurements)
    count = 0
    for value in measurements:
        if value > avg:
            count += 1
    return count


def find_value(measurements, target):
    for index in range(len(measurements)):
        if measurements[index] == target:
            return index
    return -1


def analyze_measurements(measurements):
    return find_minimum(measurements), find_maximum(measurements), calculate_average(measurements)


average = calculate_average(measurements)
minimum = find_minimum(measurements)
maximum = find_maximum(measurements)
above = count_above_average(measurements)

mn, mx, avg = analyze_measurements(measurements)

target = float(input("Введите значение для поиска: "))
position = find_value(measurements, target)

print(f"{len(measurements)}")
print(f"{minimum}")
print(f"{maximum}")
print(f"{average:.2f}")
print(f"{above}")

if position >= 0:
    print(f"Значение {target} найдено на позиции {position}")
else:
    print(f"Значение {target} не найдено")

print(f"{mn}, {mx}, {avg:.2f}")

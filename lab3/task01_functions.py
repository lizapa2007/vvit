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

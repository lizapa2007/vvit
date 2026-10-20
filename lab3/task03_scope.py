value = 10


def example():
    value = 20
    local = 30
    print(value, local)


example()
print(value)

# Обращение к локальной переменной снаружи функции -> NameError
print(local)

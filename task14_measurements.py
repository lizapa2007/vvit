n = int(input("Введите количество измерений: "))

total = 0

for i in range(n):
    v = float(input(f"Введите измерение {i + 1}: "))
    total += v

print(f"Сумма измерений: {total}")
print(f"Среднее арифметическое: {total / n}")

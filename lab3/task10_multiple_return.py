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

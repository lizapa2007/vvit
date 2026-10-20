numbers = [-10, 3, -2, 8, -5]

normal_sorted = sorted(numbers)
print(normal_sorted)

abs_sorted = sorted(numbers, key=lambda x: abs(x))
print(abs_sorted)

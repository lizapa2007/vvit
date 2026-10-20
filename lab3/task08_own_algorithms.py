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

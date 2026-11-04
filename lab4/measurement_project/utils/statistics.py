def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)


def find_min(numbers):
    minimum = numbers[0]
    for number in numbers[1:]:
        if number < minimum:
            minimum = number
    return minimum


def find_max(numbers):
    maximum = numbers[0]
    for number in numbers[1:]:
        if number > maximum:
            maximum = number
    return maximum


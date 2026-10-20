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

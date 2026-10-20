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

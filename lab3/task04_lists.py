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

def find_element(numbers, target):
    for index in range(len(numbers)):
        if numbers[index] == target:
            return index
    return -1


data = [10, 20, 30, 40, 50]

print(find_element(data, 30))
print(find_element(data, 50))
print(find_element(data, 99))

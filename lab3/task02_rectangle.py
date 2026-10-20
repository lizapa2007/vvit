def calculate_rectangle(width, height):
    return width * height


def calculate_perimeter(width, height):
    return 2 * (width + height)


def describe_rectangle(width, height, unit="cm"):
    area = calculate_rectangle(width, height)
    perimeter = calculate_perimeter(width, height)
    print(f"Прямоугольник: {width} x {height} {unit}")
    print(f"Площадь: {area} кв. {unit}")
    print(f"Периметр: {perimeter} {unit}")


describe_rectangle(6, 2)
print()
describe_rectangle(11, 9, unit="м")

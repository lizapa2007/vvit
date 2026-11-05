from pathlib import Path

from utils.reader import read_numbers, validate_numbers
from utils.statistics import calculate_average, find_min, find_max


def main():
    print("Текущий рабочий каталог:", Path.cwd())

    input_file = Path("data") / "measurements.txt"
    print("Файл существует:", input_file.exists())

    Path("logs").mkdir(exist_ok=True)

    try:
        numbers = read_numbers(input_file)
        validate_numbers(numbers)
    except FileNotFoundError:
        print("Файл не найден:", input_file)
    except ValueError as error:
        print("Ошибка в данных:", error)
    else:
        print("Прочитано значений:", len(numbers))
        print("Среднее:", calculate_average(numbers))
        print("Минимум:", find_min(numbers))
        print("Максимум:", find_max(numbers))
    finally:
        print("Обработка файла завершена")


if __name__ == "__main__":
    main()
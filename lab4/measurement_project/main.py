from pathlib import Path

from utils.reader import read_numbers
from utils.statistics import calculate_average, find_min, find_max


def main():
    print("Текущий рабочий каталог:", Path.cwd())

    input_file = Path("data") / "measurements.txt"
    print("Путь к файлу:", input_file)
    print("Файл существует:", input_file.exists())

    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    numbers = read_numbers(input_file)
    print("Прочитано значений:", len(numbers))
    print("Среднее:", calculate_average(numbers))
    print("Минимум:", find_min(numbers))
    print("Максимум:", find_max(numbers))


if __name__ == "__main__":
    main()
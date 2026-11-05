import logging
from pathlib import Path

from utils.reader import read_numbers, validate_numbers
from utils.statistics import calculate_average, find_min, find_max


def setup_logging():
    Path("logs").mkdir(exist_ok=True)
    logging.basicConfig(
        filename="logs/app.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        encoding="utf-8",
    )


def main():
    setup_logging()
    logging.info("Программа запущена")

    input_file = Path("data") / "measurements.txt"

    try:
        numbers = read_numbers(input_file)
        logging.info(f"Файл прочитан: {input_file}")
        logging.info(f"Прочитано значений: {len(numbers)}")
        validate_numbers(numbers)
    except FileNotFoundError:
        print("Файл не найден:", input_file)
        logging.error(f"Файл не найден: {input_file}")
    except ValueError as error:
        print("Ошибка в данных:", error)
        logging.error(f"Некорректные данные: {error}")
    else:
        print("Количество значений:", len(numbers))
        print("Минимум:", find_min(numbers))
        print("Максимум:", find_max(numbers))
        print("Среднее:", calculate_average(numbers))
    finally:
        logging.info("Программа завершена")


if __name__ == "__main__":
    main()
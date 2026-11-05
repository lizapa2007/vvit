import json
import logging
from pathlib import Path

from utils.reader import read_numbers, validate_numbers
from utils.statistics import calculate_average, find_min, find_max


def load_config():
    with open("config.json", "r", encoding="utf-8") as file:
        return json.load(file)


def setup_logging(log_file):
    log_file.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        encoding="utf-8",
    )


def main():
    config = load_config()
    input_file = Path(config["input_file"])
    log_file = Path(config["log_file"])

    setup_logging(log_file)
    logging.info("Программа запущена")
    print("Файл данных из config.json:", input_file)

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
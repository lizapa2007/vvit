from utils.statistics import calculate_average, find_min, find_max

def main():
    numbers = [42, 38, 51, 35, 57]
    print(numbers)
    print(calculate_average(numbers))
    print(find_min(numbers))
    print(find_max(numbers))

print(__name__)

if __name__ == "__main__":
    main()
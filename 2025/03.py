from aocd import get_data


def parse_data(data):
    lines = data.strip().split("\n")
    numbers = [[int(char) for char in line] for line in lines]
    return numbers


def find_max_two_digit_number(arr_numbers):
    # 1. Find max number in the grid, exclude last number, return index
    digit0 = max(arr_numbers[:-1])
    index0 = arr_numbers.index(max(arr_numbers[:-1]))

    # 2. Find new next max number in grid
    digit1 = max(arr_numbers[index0 + 1 :])
    return digit0 * 10 + digit1


def part1(data):
    numbers = parse_data(data)
    sum_max_numbers = 0
    for arr_numbers in numbers:
        max_two_digit_number = find_max_two_digit_number(arr_numbers)
        sum_max_numbers += max_two_digit_number
    return sum_max_numbers


def find_max_12_digit_number(arr_numbers):
    length = len(arr_numbers)
    number = 0
    index = -1
    for i in range(12):
        start_index = index + 1
        stop_index = length - (11 - i)
        digit = max(arr_numbers[start_index:stop_index])
        index = arr_numbers.index(digit, start_index, stop_index)
        number += digit * (10 ** (11 - i))
    return number


def part2(data):
    numbers = parse_data(data)
    sum_max_numbers = 0
    for arr_numbers in numbers:
        max_12_digit_number = find_max_12_digit_number(arr_numbers)
        print(max_12_digit_number)
        sum_max_numbers += max_12_digit_number
    return sum_max_numbers


example_data = """987654321111111
811111111111119
234234234234278
818181911112111"""
data = get_data(year=2025, day=3)
print(part1(data))
print(part2(data))

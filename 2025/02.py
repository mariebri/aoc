import re
from aocd import get_data


def parse_data(data):
    ranges = [x for x in data.split(",")]
    ranges = [(int(x), int(y)) for x, y in (s.split("-") for s in ranges)]
    return ranges


def is_invalid_id(id_number):
    id_str = str(id_number)
    id_length = len(id_str)
    if id_length % 2 != 0:
        return False
    part1 = id_str[: id_length // 2]
    part2 = id_str[id_length // 2 :]
    if part1 == part2:
        return True
    return False


def part1(data):
    ranges = parse_data(data)
    invalid_sum = 0
    for id_range in ranges:
        for id_number in range(id_range[0], id_range[1] + 1):
            if is_invalid_id(id_number):
                invalid_sum += id_number
    print(f"Sum of invalid IDs: {invalid_sum}")
    return invalid_sum


def is_repeated_pattern(num_str):
    return re.fullmatch(r"(\d+)\1+", num_str) is not None


def part2(data):
    ranges = parse_data(data)
    invalid_sum = 0
    for id_range in ranges:
        for id_number in range(id_range[0], id_range[1] + 1):
            if is_repeated_pattern(str(id_number)):
                invalid_sum += id_number
    print(f"Sum of invalid IDs: {invalid_sum}")
    return invalid_sum


example_data = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
data = get_data(year=2025, day=2)
part1(data)
part2(data)

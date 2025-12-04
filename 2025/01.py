from aocd import get_data
from functools import lru_cache


@lru_cache(maxsize=None)
def update_pointer(pointer, rotation, delta):
    # Left = Minus, Right = Plus
    if rotation == "L":
        return (pointer - delta) % 100
    elif rotation == "R":
        return (pointer + delta) % 100
    else:
        raise ValueError("Invalid rotation direction")


def part1(data):
    no_zero = 0
    pointer = 50
    for line in data.splitlines():
        rotation = line[0]
        delta = int(line[1:])
        pointer = update_pointer(pointer, rotation, delta)
        if pointer == 0:
            no_zero += 1
    return no_zero


@lru_cache(maxsize=None)
def count_zero_passings(pointer, rotation, delta):
    count = 0
    delta_parts = delta // 100
    delta_remainder = delta % 100
    delta_split = (
        [100] * delta_parts + [delta_remainder]
        if delta_remainder > 0
        else [100] * delta_parts
    )

    for split in delta_split:
        if rotation == "L":
            if pointer - split <= 0 and pointer != 0:
                count += 1
            pointer = (pointer - split) % 100
        elif rotation == "R":
            if pointer + split >= 100 and pointer != 0:
                count += 1
            pointer = (pointer + split) % 100
    return count, pointer


@lru_cache(maxsize=None)
def count_each_passing(pointer, rotation, delta):
    count = 0
    for step in range(1, delta + 1):
        if rotation == "L":
            pointer = (pointer - 1) % 100
        elif rotation == "R":
            pointer = (pointer + 1) % 100
        if pointer == 0:
            count += 1
    return count, pointer


def part2(data):
    no_zero = 0
    pointer = 50
    for line in data.splitlines():
        rotation = line[0]
        delta = int(line[1:])
        count, pointer = count_each_passing(pointer, rotation, delta)
        no_zero += count
    return no_zero


example_data = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""
data = get_data(year=2025, day=1)
print(part1(data))
print(part2(data))

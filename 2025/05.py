from aocd import get_data


def parse_data(data):
    sections = data.strip().split("\n\n")

    # Store ranges as (start, end) tuples
    ranges = []
    for line in sections[0].splitlines():
        start, end = map(int, line.split("-"))
        ranges.append((start, end))

    numbers = [int(x) for x in sections[1].splitlines()]
    return ranges, numbers


def merge_ranges(ranges):
    # Sort by start
    ranges = sorted(ranges, key=lambda x: x[0])
    merged = [ranges[0]]

    for curr_start, curr_end in ranges[1:]:
        last_start, last_end = merged[-1]

        # If overlapping or adjacent → merge
        if curr_start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, curr_end))
        else:
            merged.append((curr_start, curr_end))

    return merged


def part1(data):
    ranges, numbers = parse_data(data)
    ranges = merge_ranges(ranges)
    count = sum(any(start <= x <= end for start, end in ranges) for x in numbers)
    return count


def part2(data):
    ranges, _ = parse_data(data)
    ranges = merge_ranges(ranges)
    total_covered = sum(end - start + 1 for start, end in ranges)
    return total_covered


example_data = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
data = get_data(day=5, year=2025)
print(part1(data))
print(part2(data))

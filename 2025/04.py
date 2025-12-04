from aocd import get_data


def parse_data(data):
    lines = data.strip().split("\n")
    grid = [[char for char in line] for line in lines]
    return grid


def find_neighbors(x, y, grid):
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            neighbors.append((nx, ny))
    return neighbors


def find_removable_points(grid):
    removable_points = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "@":
                neighbors = find_neighbors(x, y, grid)
                if sum(1 for nx, ny in neighbors if grid[ny][nx] == "@") < 4:
                    removable_points.append((x, y))
    return removable_points


def update_grid(grid, removable_points):
    new_grid = grid.copy()
    for x, y in removable_points:
        new_grid[y][x] = "."
    return new_grid


def part1(data):
    grid = parse_data(data)
    remov_points = find_removable_points(grid)
    return len(remov_points)


def part2(data):
    grid = parse_data(data)
    remov_points = find_removable_points(grid)
    removed_count = 0
    while remov_points:
        grid = update_grid(grid, remov_points)
        removed_count += len(remov_points)
        remov_points = find_removable_points(grid)
    return removed_count


example_data = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
data = get_data(year=2025, day=4)
print(part1(data))
print(part2(data))

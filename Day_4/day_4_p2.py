with open("./day_4.txt") as file:
    lines = file.read().strip().split("\n")

n = len(lines)
m = len(lines[0])

grid = []

# Convert to a 2D array so we can change its contents
for line in lines:
    grid.append(list(line))

directions = {(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)}

def within_bounds(x, y) -> bool:
    return 0 <= x < n and 0 <= y < m

def get_neighbors(x, y) -> int:
    neighbors = 0

    for dir in directions:
        xx = x + dir[0]
        yy = y + dir[1]

        if within_bounds(xx, yy) and grid[xx][yy] == '@':
            neighbors += 1

    return neighbors

rolls = 0
toRemove = []

# Loop until we can no longer remove a roll

while True:

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '@' and get_neighbors(i, j) < 4:
                toRemove.append((i, j))

    for roll in toRemove:
        grid[roll[0]][roll[1]] = '.'

    if len(toRemove) == 0:
        break
    else:
        rolls += len(toRemove)
        toRemove.clear()

print(rolls)

# Remove the found rolls and keep repeating until no more rolls can be removed.
# Answer: 8701
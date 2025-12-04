with open("./day_4.txt") as file:
    lines = file.read().strip().split("\n")

n = len(lines)
m = len(lines[0])

directions = {(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)}

def within_bounds(x, y) -> bool:
    return 0 <= x < n and 0 <= y < m

def get_neighbors(x, y) -> int:
    neighbors = 0

    for dir in directions:
        xx = x + dir[0]
        yy = y + dir[1]

        if within_bounds(xx, yy) and lines[xx][yy] == '@':
            neighbors += 1

    return neighbors

rolls = 0

for i in range(n):
    for j in range(m):
        if lines[i][j] == '@' and get_neighbors(i, j) < 4:
            rolls += 1

print(rolls)

# If a point in the grid is a @, count its neighbors within 1 tile (diagonal included) and see if its neighbors are less than 4 (also @).
# Answer: 1451
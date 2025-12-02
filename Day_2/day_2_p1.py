with open("./day_2.txt") as file:
    lines = file.read().strip().split(",")

sum = 0

for line in lines:
    start, end = line.split("-")
    for id in range(int(start), int(end) + 1):
        num = str(id)
        midpoint = len(num) // 2
        if len(num) % 2 == 0 and num[:midpoint] == num[midpoint:]:
            sum += id

print(sum)

# Invalid ID is the IDs that have a pattern that repeats twice
# Answer: 38158151648
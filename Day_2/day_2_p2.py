with open("./day_2.txt") as file:
    lines = file.read().strip().split(",")

sum = 0

for line in lines:
    start, end = line.split("-")
    for id in range(int(start), int(end) + 1):
        num = str(id)

        if len(num) == 1:
            continue

        windowLength = 1
        while windowLength <= len(num) // 2:

            potentialPattern = num[0:0+windowLength]
            idx = 0

            windowLength += 1


print(sum)

# Invalid ID is the IDs that have a pattern that repeats AT LEAST twice
# Answer: 
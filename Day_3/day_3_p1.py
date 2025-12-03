with open("./day_3.txt") as file:
    lines = file.read().strip().split("\n")

joltage = 0

for line in lines:
    highestLeftDigit = 1
    for i in range(len(line)-1):
        digit = int(line[i])

        if digit > highestLeftDigit:
            highestLeftDigit = digit

    # Find first instance of the highest left digit and then loop from the back to find the highest right digit up until this point
    instance = line.index(str(highestLeftDigit))
    highestRightDigit = 1

    idx = len(line) - 1
    while idx > instance:

        digit = int(line[idx])

        if digit > highestRightDigit:
            highestRightDigit = digit

        idx -= 1

    joltage += int(str(highestLeftDigit) + str(highestRightDigit))
        
print(joltage)

# Find two digits within a line where it is the largest and must be read left to right. Add up all of these digits.
# Answer: 17142
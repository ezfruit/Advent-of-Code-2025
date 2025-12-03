with open("./day_3.txt") as file:
    lines = file.read().strip().split("\n")

joltage = 0

DIGITS = 12

for line in lines:
    nums = []
    instance = 0

    # Find the highest digit 12 times
    for i in range(DIGITS):
        highestDigit = 1
        
        # Only look for the highest digit within this bounds
        for j in range(instance, len(line) - (DIGITS - i - 1)):
        
            digit = int(line[j])

            if digit > highestDigit:
                highestDigit = digit

        # Set the left bound to the last digit's index found + 1
        instance = line[instance:].index(str(highestDigit)) + instance + 1
        nums.append(str(highestDigit))

    joltage += int("".join(nums))
        
print(joltage)

# This code also works for part 1 by swapping the DIGITS constant to 2.
# Find TWELVE digits within a line where it is the largest and must be read left to right. Add up all of these digits.
# Answer: 169935154100102
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
        # We use a sliding window algorithm that checks each pattern length of 1 up to length / 2 to check if it repeats
        while windowLength <= len(num) // 2:

            potentialPattern = num[:windowLength]
            idx = 0

            invalid = True

            while idx + windowLength < len(num):

                idx += windowLength
                
                if num[idx:idx+windowLength] == potentialPattern:
                    potentialPattern = num[idx:idx+windowLength]
                else:
                    invalid = False
                    break

            if invalid:
                sum += id
                break

            windowLength += 1

print(sum)

# Invalid ID is the IDs that have a pattern that repeats AT LEAST twice
# Answer: 45283684555
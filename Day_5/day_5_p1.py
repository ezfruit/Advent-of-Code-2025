with open("./day_5.txt") as file:
    lines = file.read().strip().split("\n\n")

ranges = lines[0].split("\n")
available = lines[1].split("\n")

store = {}

for range in ranges:
    start, end = range.split("-")
    startNumber = int(start)
    endNumber = int(end)
    # Update the range only if it's better
    if startNumber in store:
        if endNumber > store[startNumber]:
            store[startNumber] = endNumber
    else:
        store[startNumber] = endNumber

count = 0

for num in available:
    for key in store.keys():
        number = int(num)
        # If within range, update the count
        if number >= key and number <= store[key]:
            count += 1
            break

print(count)

# Find the number of fresh ingredients given a list of fresh ranges and a list of available ingredients
# Answer: 598
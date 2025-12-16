with open("./day_5.txt") as file:
    lines = file.read().strip().split("\n\n")

ranges = lines[0].split("\n")

intervalRanges = []

# Convert all ranges to a tuple of start and end ranges that are ints
for range in ranges:
    start, end = range.split("-")
    startNum, endNum = int(start), int(end)
    intervalRanges.append((startNum, endNum))

# Sort them so our algo can greedily count based on the intervals
intervalRanges.sort()

bestStartTime = 0
bestEndTime = -1

intervals = []

for range in intervalRanges:
    start, end = range[0], range[1]
    if start > bestEndTime:
        intervals.append((bestStartTime, bestEndTime))
        bestStartTime = start
        bestEndTime = end
    elif end > bestEndTime:
        bestEndTime = end


intervals.append((bestStartTime, bestEndTime))

# No overlapping intervals at this point

count = 0

# At this point, we just need to count up the difference between the end and start
for i in intervals:
    start, end = i[0], i[1]
    count += end - start + 1
    
print(count)

# Find the total number of fresh ingredients based on just the ranges alone
# Answer: 360341832208407


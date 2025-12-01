with open("./day_1.txt") as file:
    lines = file.read().strip().split("\n")

dial = 50
password = 0

for line in lines:
    if line[0] == 'L':
        dial = (dial - int(line[1:])) % 100
    else:
        dial = (dial + int(line[1:])) % 100

    if dial == 0:
        password += 1

print(password)

# Password is number of times the dial hits 0
# Answer: 982
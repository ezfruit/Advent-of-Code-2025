with open("./day_1.txt") as file:
    lines = file.read().strip().split("\n")

dial = 50
password = 0

for line in lines:
    if line[0] == 'L':
        # If passes 0 and it wasn't a 0 to start
        if dial - int(line[1:]) <= 0 and dial != 0:
            password += abs(dial - int(line[1:])) // 100 + 1
        # If passes 0 and it was a 0 to start
        elif dial - int(line[1:]) <= 0:
            password += abs(dial - int(line[1:])) // 100
        # Doesn't pass 0
        dial = (dial - int(line[1:])) % 100
    else:
        password += (dial + int(line[1:])) // 100
        dial = (dial + int(line[1:])) % 100

print(password)

# Password is number of times 0 is passed either during rotation or on a stop
# Answer: 6106
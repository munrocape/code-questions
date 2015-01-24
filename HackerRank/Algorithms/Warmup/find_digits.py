lines = input()

for line in range(lines):
    number = raw_input()
    count = 0
    for digit in s:
        if digit != 0:
            if int(num) % int(digit) == 0:
                count += 1
    print count
def find_pair(dollars, flavours):
    length = len(flavours)
    for i in range(length):
        for j in range(i + 1, length):
            a = flavours[i]
            b = flavours[j]
            if a + b == dollars:
                return str(i + 1) + ' ' + str(j + 1)


cases = int(raw_input())
for i in range(cases):
    dollars = int(raw_input())
    flavours = int(raw_input())
    cost_array = map(int, raw_input().split(' '))
    print find_pair(dollars, cost_array)
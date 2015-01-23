import math
T = int(raw_input())
for i in range (0,T):
    low, high = [int(x) for x in raw_input().split(' ')]
    start_root = int(math.ceil(low ** 0.5))
    high_root = int(math.ceil(high ** 0.5))
    answer = 0
    while start_root <= high_root:
        if (start_root ** 2) <= high:
            answer += 1
        start_root += 1
    print answer
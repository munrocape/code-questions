# Maintaining the jar totals can be very expensive for large values of N
N, M = [int(x) for x in raw_input().split(' ')]
total = 0
for i in range (M):
    a, b, k = [int(x) for x in raw_input().split(' ')]
    a -= 1
    total += k * (b - a)
print total / N
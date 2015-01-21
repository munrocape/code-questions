n = input()
k = input()
candies = [input() for _ in range(0,n)]
candies.sort()
min_diff = candies[-1]
i = 0
j = k - 1
elements = len(candies)
while j < elements:
    diff = candies[j] - candies[i]
    if diff < min_diff:
        min_diff = diff
    i += 1
    j += 1

print min_diff
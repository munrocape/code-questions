def determine_num_changes(s):
    index = 0
    length = len(s)
    halfway = length / 2
    deletions = 0
    while index < halfway:
        deletions += abs(ord(s[index]) - ord(s[length - 1 - index]))
        index += 1
    return deletions

n = int(raw_input())
for i in range(0, n):
    s = raw_input()
    print determine_num_changes(s)
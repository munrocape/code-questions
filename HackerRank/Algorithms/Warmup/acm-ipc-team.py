'''
# Iterative solution in the order of n^2

contestant_count, question_count = map(int,raw_input().split())
contestants = []
for i in range(contestant_count):
    contestants.append(raw_input())

max_knowledge = 0
teams = 0
for i in range(contestant_count):
    for j in range(i+1, contestant_count):
        knowledge = len([x for x, y in zip(contestants[i], contestants[j]) if (x == '1') or (y == '1')])
        if knowledge > max_knowledge:
            max_knowledge = knowledge
            teams = 1
        elif knowledge == max_knowledge:
            teams += 1
print max_knowledge
print teams
'''


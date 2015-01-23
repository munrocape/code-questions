T = int(raw_input())
for i in range (0,T):
    cash, cost_of_chocolate, wrappers_per_chocolate = [int(x) for x in raw_input().split(' ')]
    
    answer = 0
    wrappers = 0
    answer = cash / cost_of_chocolate
    wrappers = answer
    while wrappers >= wrappers_per_chocolate:
        new_wrappers = wrappers / wrappers_per_chocolate
        answer += new_wrappers
        wrappers = (wrappers % wrappers_per_chocolate) + new_wrappers
    
    print answer
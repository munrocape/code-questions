def get_fib(requested_index, known_fib=[0, 1]):
    
    total_known = len(known_fib) 
    
    if total_known > requested_index:    
        return known_fib[requested_index]
    
    second_to_last_known = known_fib[-2]
    last_known = known_fib[-1]
    
    for i in range(1 + requested_index - total_known):
        a = second_to_last_known
        b = last_known
        last_known = a + b
        second_to_last_known = b
        known_fib.append(last_known)  
    
    return known_fib[requested_index]

test_cases = input()
for i in range(test_cases):
    num = input()
    n = 1
    fib = get_fib(n)
    while fib < num:
        fib = get_fib(n)
        n += 1
    if fib  == num:
        print 'IsFibo'
    else:
        print 'IsNotFibo'
def lonelyinteger(a):
    answer = 0
    for element in a:
    	# anything XOR'ed itself is 0. So in a chain of a XOR a XOR b XOR b XOR c XOR 0, the result will be c - the lonely number
        answer = answer ^ element
    return answer

if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)

def flip(n):
    return 4294967295 - n
n = int(raw_input())
for i in range(0,n):
    num = raw_input()
    num = int(num)
    res = flip(num)
    print res
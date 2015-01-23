T = int(raw_input())
for i in range (0,T):
    max_cuts = int(raw_input())
    if max_cuts % 2 == 1:
        print (max_cuts / 2) * ((max_cuts / 2) + 1)
    else:
        print (max_cuts / 2) ** 2
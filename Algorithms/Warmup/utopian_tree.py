def spring(growth_cycles_remaining, height):
    if growth_cycles_remaining == 0:
        return height
    height = height * 2
    return summer(growth_cycles_remaining-1, height)

def summer(growth_cycles_remaining, height):
    if growth_cycles_remaining == 0:
        return height
    height = height + 1
    return spring(growth_cycles_remaining-1, height)

n = int(raw_input())
for i in range(0,n):
    growth_cycles = raw_input()
    growth_cycles = int(growth_cycles)
    res = spring(growth_cycles, 1)
    print res
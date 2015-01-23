def print_possible_values(stone_count, low_delta, high_delta):
    if low_delta == high_delta:
        print (stone_count - 1) * low_delta
    else:
        stone_str = ''
        for i in range(stone_count):
            stone_str += str((low_delta * (stone_count - 1 - i)) + (high_delta * i)) + ' '
        print stone_str

T = int(raw_input())
for i in range (0,T):
    stone_count = int(raw_input())
    delta_a = int(raw_input())
    delta_b = int(raw_input())
    if delta_a < delta_b:
        print_possible_values(stone_count, delta_a, delta_b)
    else:
        print_possible_values(stone_count, delta_b, delta_a)
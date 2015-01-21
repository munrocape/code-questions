string = raw_input()
 
found = False

frequency_array = {}
for c in 'abcdefghijklmnopqrstuvwxyz':
    frequency_array[c] = 0

for c in string:
    frequency_array[c] += 1

center_found = False
palindrome = True
for value in frequency_array.values():
    if value % 2 == 1:
        if center_found:
            palindrome = False
            break
        else:
            center_found = True
            
if palindrome:
    print("YES")
else:
	print("NO")
    
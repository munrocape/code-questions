s = raw_input().lower()
unique_characters = 0
is_pangram = False
char_dict = {}
for char in s:
    if char != ' ':
        if char not in char_dict:
            char_dict[char] = 1
            unique_characters += 1
        	if unique_characters == 26:
            	is_pangram = True
            	break
if is_pangram:
    print "pangram"
else:
    print "not pangram"
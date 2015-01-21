def recursive_determine_deletions(s, index_a, index_b, deletions):
	'''Maximum input size of 10^5. Consider the impact of recursing over such a string on the call stack.'''
	if index_a == len(s) or index_b == len(s):
		return deletions
	elif s[index_a] == s[index_b]:
		return recursive_determine_deletions(s, index_a, index_b + 1, deletions + 1)
	else:
		return recursive_determine_deletions(s, index_b, index_b + 1, deletions)


def iterative_determine_deletions(s):
    index_a = 0
    index_b = 1
    deletions = 0
    while(index_b != len(s)):
        if s[index_a] == s[index_b]:
            deletions += 1
            index_b += 1
        else:
            index_a = index_b
            index_b += 1
    return deletions
       

n = int(raw_input())
for i in range(0,n):
    s = raw_input()
    #print recursive_determine_deletions(s, 0, 1, 0)
    print iterative_determine_deletions(s)
'''
	[3,5] 		[3,6]
			[4,5] [5,6][6,7]
			[4,6][6,8]
	3: [4,5][5,6][6,7]
'''

def answer(meetings):
	sort = sorted(meetings)
	uniq = []
	for x in sort:
		if x not in uniq:
			uniq.append(x)
	print uniq
	meetings = []
	for x in range(0, len(uniq) - 1):
		print x
		if (uniq[x][1] - 1 in range(uniq[x + 1][0], uniq[x + 1][1])):

	print meetings	
	return len(meetings)

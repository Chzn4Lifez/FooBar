def answer(n):
	i = 0
	count = 0
	x = 1
	a = n
	while (a > 0):
		x = 0
		i = 1
		while (x <= a):
			x = i * i
			i = i + 1
		x = (i - 2) * (i - 2)
		a = a - x
		# print 'n is %d substracting %d -> %d' % (n + x, x, n)
		count = count + 1
	return count

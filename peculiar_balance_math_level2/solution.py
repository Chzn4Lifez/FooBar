nswer(x):
	n = 1
	an = 1
	while (an <= x):
		an = (3**n + 1)/2
		n += 1
	n += -2
	list = []
	for a in range(0, n + 1):
		index = (3**a + 1)/2
		mult = 3**a
		num = x
		# Simplify to the first mult
		if (index != 1):
			reduced = num - index
		else:
			reduced = num
		reduced = (reduced % (mult * 3))
		if (a == 0):
			if reduced%3 == 0:
				list.append("-")
			if reduced%3 == 1:
				list.append("R")
			if reduced%3 == 2:
				list.append("L")
		else:
			if (reduced in range(0, mult)):
				list.append("R")
			if (reduced in range(mult, (mult * 2))):
				list.append("L")
			if (reduced in range((mult * 2), (mult * 3))):
				list.append("-")
	return list

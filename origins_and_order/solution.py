def answer(x, y, z):
	sort = sorted([x, y, z])
	time = str(sort[0]) + "/" + str(sort[1]) + "/" + str(sort[2])
	a = sort[0]
	b = sort[1]
	c = sort[2]
		
	# February
	if (a == 2) and (b > 28):
		return "Ambiguous"
	if (a == 2) and (c < 29) and (c != b):
		return "Ambiguous"
	
	# Months with 30 days
	if (a in [4, 6, 9, 11]) and (b > 30):
		return "Ambiguous"
	if (a in [4, 6, 9, 11]) and (c < 31) and (c != b):
		return "Ambiguous"
	
	# Repeats: Same Month/Day + Year/Month
	if (b < 13) and (b != a):
		return "Ambiguous"
	if (c < 32) and (c != b):
		return "Ambiguous"
	
	# Constraints to double check everything
	if (b > 31):
		return "Ambiguous"
	if (a > 12):
		return "Ambiguous"
	if (a < 10):
		a = "0" + str(a)
	if (b < 10):
		b = "0" + str(b)
	if (c < 10):
		c = "0" + str(c)
	return str(a) + "/" + str(b) + "/" + str(c)

def answer(x):
	employees = 1
	for level in range(x):
		total = (employees * 7) + 1
		employees = total
	return total


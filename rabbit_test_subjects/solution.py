def answer(x, y):
	import math
	a = sum(float(item) for item in x)
	b = sum(float(item) for item in y)
	c = (b - a)/b
	return math.trunc(c * 100)

from dateutil import parser

def parse(string, agnostic=True, **kwargs):
    try:
	    # if agnostic or parser.parse(string, **kwargs) == parser.parse(string, yearfirst=True, **kwargs) == parser.parse(string, dayfirst=True, **kwargs):
        print parser.parse(string, **kwargs)
    except ValueError:
    	print("The date was ambiguous: %s" % string)
        
def answer(x, y, z):
	sort = sorted([x, y, z])
	a = sort[0]
	b = sort[1]
	c = sort[2]
	
	time = ""
	if (a < 10):
		time += "0" + str(a) + "/"
	elif (a >= 10):
		time += str(a) + "/"
	if (b < 10):
		time += "0" + str(b) + "/"
	elif (b >= 10):
		time += str(b) + "/"
	if (c < 10):
		time += "0" + str(c)
	elif (c >= 10):
		time += str(c)


	# February
	if (a == 2) and (b > 28):
		return "Ambiguous"
	if (a == 2) and (b < 13) and (b != a):
		return "Ambiguous"
	if (a == 2) and (c < 29) and (c != b):
		return "Ambiguous"
	elif (a == 2):
		return time 

	# Months with 30 days
	if (a in [4, 6, 9, 11]) and (b > 30):
		return "Ambiguous"
	if (a in [4, 6, 9, 11]) and (b < 13) and (b != a):
		return "Ambiguous"
	if (a in [4, 6, 9, 11]) and (c < 31) and (c != b):
		return "Ambiguous"
	elif (a in [4, 6, 9, 11]):
		return time
	
	
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
	return time 
'''
for x in range(1, 99):
	for y in range(1, 99):
		for z in range(1, 99):
			if (answer(x, y, z) != 'Ambiguous'):
				try:
					parser.parse(answer(x, y, z))
				except ValueError:
					print answer(x, y, z)
			if (answer(x, y, z) == 'Ambiguous'):
				try:
					parser.parse(answer(x, y, z))
				except ValueError:
					continue
'''

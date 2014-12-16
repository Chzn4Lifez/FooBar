def answer(digest):
	message = [0]
	for i in range(0, len(digest)):
		x = digest[i] ^ message[i]
		y = x * 129
		z = y % 256
		message.append(z)
	        # print "%d * 129 \t->\t %d ^ %d  \t->\t %d MOD 256 \t->\t %d " % (digest[i], x, message[i], y, z) 
	message.remove(0)
	return message

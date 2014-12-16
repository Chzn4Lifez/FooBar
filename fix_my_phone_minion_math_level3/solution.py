def answer(x, y, z):
	DP = [[[0 for a in range(0, z + 1)] for b in range(0, 10)] for c in range(0, 10)]
	moves=[[4,6],[6,8],[7,9],[4,8],[0,3,9],[],[0,1,7],[2,6],[1,3],[2,4]]
	for a in range(0, 10):
		for b in range(0, 10):
			if (b in moves[a]):
				DP[a][b][1] = 1
	for c in range(2, z + 1):
		for a in range(0, 10):
			for b in range(0, 10):
				for d in range(0, 10):
					if (b in moves[d]):
						DP[a][b][c] = DP[a][b][c] + DP[a][d][c - 1];
	return DP[x][y][z - 1]

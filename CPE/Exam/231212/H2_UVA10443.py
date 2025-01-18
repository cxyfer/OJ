""" UVA 10443 - Rock, Scissors, Paper
	Simulation
	CPE 能 AC；但在 UVA 上用 Python 會 TLE ，需改用 C++ 
"""
T = int(input())

for tc in range(T):
	r, c, n = map(int, input().split())
	mp = [list(input()) for _ in range(r)] # map
	tmp = [[-1 for _ in range(c)] for _ in range(r)] # temp map
	for d in range(n): # days
		for i in range(r):
			for j in range(c):
				tmp[i][j] = mp[i][j]
		for i in range(r):
			for j in range(c):
				for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
					if x < 0 or x >= r or y < 0 or y >= c:
						continue
					if mp[x][y] == "R" and mp[i][j] == "S":
						tmp[i][j] = "R"
					if mp[x][y] == "S" and mp[i][j] == "P":
						tmp[i][j] = "S"
					if mp[x][y] == "P" and mp[i][j] == "R":
						tmp[i][j] = "P"
		for i in range(r): # update
			for j in range(c):
				mp[i][j] = tmp[i][j]
	for row in mp:
		print("".join(row))
	if tc < T - 1:
		print()
	

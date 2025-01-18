import sys
input = sys.stdin.readline
def print(val):
	sys.stdout.write(str(val) + '\n')

while (True):
	K = int(input())
	if not K:
		break
	N, M = map(int, input().split())
	for _ in range(K):
		X, Y = map(int, input().split())
		if X == N or Y == M:
			print("divisa")
		elif X > N and Y > M:
			print("NE")
		elif X > N and Y < M:
			print("SE")
		elif X < N and Y > M:
			print("NO")
		else:
			print("SO")
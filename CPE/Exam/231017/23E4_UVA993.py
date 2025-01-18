from collections import *

T = int(input())

for _ in range(T):
	N = int(input())
	if N == 0: # 0的話直接輸出0
		print(0)
		continue
	# 因數分解，檢查有沒有大於10的因數，注意可以合併2^3=8來縮小答案
	cnt = defaultdict(int)
	for p in range(9, 1, -1):
		while (N % p == 0):
			cnt[p] += 1
			N //= p
	if N != 1:
		print(-1)
	else:
		ans = ""
		for p in range(2, 10):
			ans += str(p) * cnt[p]
		print(ans if ans else 1)
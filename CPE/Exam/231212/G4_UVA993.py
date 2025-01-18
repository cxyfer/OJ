T = int(input())

for _ in range(T):
	N = int(input())
	if N <= 1: # 0 or 1
		print(N)
		continue
	# 因數分解，檢查有沒有大於10的因數，注意可以合併2^3=8來縮小答案
	cnt = [0] * 10
	for p in range(9, 1, -1): # [9, 2]
		while (N % p == 0):
			cnt[p] += 1
			N //= p
	if N != 1: # 有大於10的因數
		print(-1)
	else:
		ans = ""
		for p in range(2, 10):
			ans += str(p) * cnt[p]
		print(ans)
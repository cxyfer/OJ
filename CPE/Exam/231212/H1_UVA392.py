N = 8
while True:
	try:
		coef = list(map(int, input().split()))
	except EOFError:
		break
	if all(c == 0 for c in coef): # 特判
		print(0)
		continue
	flag = False # 前面是否有其他項
	for i, x in enumerate(coef):
		if not x:
			continue
		if flag:
			print(" + " if x > 0 else " - ", end = "") 
		else:
			if x < 0:
				print("-", end = "") 
			flag = True
		x = abs(x) # 係數部分
		m = N - i # 次方
		if x != 1 or m == 0:
			print(x, end = "") 
		if m > 1:
			print(f"x^{m}", end = "") 
		elif m == 1:
			print("x", end = "") 
	print()
	
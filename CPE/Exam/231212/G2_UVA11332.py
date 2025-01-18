while(True):
	n = int(input())
	if not n:
		break
	while (n >= 10):
		s = 0
		while (n):
			s += n % 10
			n //= 10
		n = s
	print(n)
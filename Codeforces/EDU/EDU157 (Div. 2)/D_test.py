import random

N = 5000
B = list(range(N))
random.shuffle(B)
A = []
for i in range(1, N):
    A.append(B[i-1] ^ B[i])

print(N)
print(*A, sep=' ', end='\n\n')
print(*B, sep=' ')
T = int(input())

for _ in range(T):
    M = int(input())
    print(bin(M).count('1'), bin(int(str(M), 16)).count('1'))
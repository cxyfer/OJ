"""
    00 -> 010 -> 00100 -> 0001000 -> ...
    11 -> 111
    01 -> 001 -> 0001 -> 00001 -> ...
    10 -> 100 -> 1000 -> 10000 -> ...
"""

T = int(input())

for _ in range(T):
    N  = int(input())
    S = input()
    if S.count("1") == N:
        print("NO")
    else:
        print("YES")

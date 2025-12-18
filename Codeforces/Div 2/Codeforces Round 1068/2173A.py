from itertools import accumulate

def solve():
    n, k = map(int, input().split())
    A = list(map(int, input()))
    
    d = [0] * n
    for i, x in enumerate(A):
        if x == 1:
            d[i] += 1
            if i + k + 1 < n:
                d[i + k + 1] -= 1
    
    s = list(accumulate(d))
    print(s.count(0))
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
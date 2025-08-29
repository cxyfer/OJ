import math

N = int(1e5)

def query(A):
    print("?", len(A), *A, flush=True)
    return int(input())

def answer(w):
    print("!", w, flush=True)

def solve():
    r1 = query([1] * N)
    if r1 == 1:
        answer(N)
        return
    
    # r1 = ceil(N / W)
    # => ceil(N / r1) <= W < ceil(N / (r1 - 1))
    L = math.ceil(N / r1)
    R = math.ceil(N / (r1 - 1)) - 1
    if L == R:
        answer(L)
        return
    
    A = []
    for x in range(1, R - L + 1):
        A.append(L)
        A.append(x)
    r2 = query(A)

    W = 2 * R - L - r2
    answer(W)
    
t = int(input())
for _ in range(t):
    solve()
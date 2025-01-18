import math

n, m, q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
queries = [int(input()) for _ in range(q)]

sum_a, sum_b = sum(A), sum(B)
S = sum_a * sum_b
st_a = {str(sum_a - A[r]) for r in range(n)}
st_b = {str(sum_b - B[c]) for c in range(m)}

for x in queries:
    if x != 0:
        factors = set()
        abs_x = abs(x)
        for i in range(1, int(math.isqrt(abs_x)) + 1):
            if abs_x % i == 0:
                factors.add(i)
                factors.add(-i)
                factors.add(x // i)
                factors.add(-x // i)
        for u in factors:
            if str(u) in st_a:
                v = x // u
                if str(v) in st_b:
                    print("YES")
                    break
        else:
            print("NO")
    else:
        print("YES" if x in st_a or x in st_b else "NO")
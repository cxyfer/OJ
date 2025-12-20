from functools import reduce
from operator import or_

def solve():
    H, W, N = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    B = [int(input()) for _ in range(N)]
    assert len(A) == H and len(A[0]) == W and len(B) == N

    msk = reduce(or_, [1 << x for x in B])
    ans = 0
    for row in A:
        cur = reduce(or_, [1 << x for x in row])
        ans = max(ans, (cur & msk).bit_count())
    print(ans)

if __name__ == "__main__":
    solve()
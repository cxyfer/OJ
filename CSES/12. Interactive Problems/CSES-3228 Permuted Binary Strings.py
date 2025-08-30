from typing import List

def query(b: str) -> str:
    print('?', b, flush=True)
    return input()

def answer(A: List[int]) -> None:
    print('!', *A, flush=True)
    return

def solve():
    n = int(input())
    A = [0] * n
    for k in range(10):
        s = ""
        for i in range(1, n + 1):
            s += '1' if (i >> k) & 1 else '0'
        B = query(s)
        for i, b in enumerate(B):
            if b == '1':
                A[i] |= (1 << k)
    answer(A)

if __name__ == "__main__":
    solve()
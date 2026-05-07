def pow(a: int, b: int, p: int) -> int:
    res = 1
    while b > 0:
        if b & 1:
            res = res * a % p
        a = a * a % p
        b >>= 1
    return res


def solve():
    a, b, p = map(int, input().split())
    print(f"{a}^{b} mod {p}={pow(a, b, p)}")


if __name__ == "__main__":
    solve()

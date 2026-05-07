from math import log10


def solve():
    P = int(input())

    # log10(2^P) = P * log10(2)
    L = int(P * log10(2)) + 1
    print(L)

    ans = pow(2, P, 10**500) - 1
    ans = f"{ans:0500d}"
    for i in range(0, 500, 50):
        print(ans[i : i + 50])


if __name__ == "__main__":
    solve()

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n

    st = []
    for x in A:
        if len(st) >= 3 and st[-1] == x and st[-2] == x and st[-3] == x:
            for _ in range(3):
                st.pop()
        else:
            st.append(x)
    print(len(st))


if __name__ == "__main__":
    solve()

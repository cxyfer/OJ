def solve():
    Q = int(input())

    # 維護 cnt_i 以及 min(cnt_1, cnt_2, ..., cnt_i)
    st1, st2 = [0], [0]
    for _ in range(Q):
        op, *args = input().split()
        if op == "1":
            c = args[0]
            st1.append(st1[-1] + (1 if c == "(" else -1))
            st2.append(min(st1[-1], st2[-1]))
        else:
            st1.pop()
            st2.pop()
        # 只有當 cnt_i == 0 且 min(cnt_1, cnt_2, ..., cnt_i) == 0 時，才能恰好匹配
        print("Yes" if st1[-1] == 0 and st2[-1] == 0 else "No")


if __name__ == "__main__":
    solve()

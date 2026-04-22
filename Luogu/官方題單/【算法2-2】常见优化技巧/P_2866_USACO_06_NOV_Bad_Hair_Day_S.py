"""
P2866 [USACO06NOV] Bad Hair Day S
https://www.luogu.com.cn/problem/P2866
Monotonic Stack

兩種思路：
1. 計算每個牛能看到的牛的數量，即找到右側第一個高度 >= 他的位置
2. 計算每個牛能被多少牛看到
"""


def solve():
    n = int(input())
    A = [int(input()) for _ in range(n)]
    assert len(A) == n

    # 計算每個牛能看到的牛的數量
    def solve1():
        ans = 0
        A.append(float("inf"))  # 哨兵
        st = [n]
        for i in range(n - 1, -1, -1):
            while st and A[i] > A[st[-1]]:
                st.pop()
            # 此時 st[-1] 為右側第一個高度 >= A[i] 的位置
            ans += st[-1] - i - 1
            st.append(i)
        return ans

    def solve2():
        ans = 0
        st = []  # 保存能看到當前牛的牛的位置
        for i, h in enumerate(A):
            while st and h >= A[st[-1]]:
                st.pop()
            ans += len(st)
            st.append(i)
        return ans

    print(solve1())
    # print(solve2())


if __name__ == "__main__":
    solve()

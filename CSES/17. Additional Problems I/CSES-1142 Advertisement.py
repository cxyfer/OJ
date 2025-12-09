"""
CSES-1142 Advertisement
https://cses.fi/problemset/task/1142
Same as 84. Largest Rectangle in Histogram

Monotonic Stack
"""
def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n
    A = [0] + A + [0]  # 在兩端添加 0 做為哨兵，方便處理邊界情況

    ans = 0
    st = []  # 單調遞增，保存的是下標
    for i, x in enumerate(A):
        while st and A[st[-1]] > x:
            # 以 A[st.pop()] 為最大高度的矩形，可以橫跨 [st[-1] + 1, i - 1]
            h = A[st.pop()]
            w = i - st[-1] - 1
            ans = max(ans, h * w)
        st.append(i)
    print(ans)

if __name__ == "__main__":
    solve()
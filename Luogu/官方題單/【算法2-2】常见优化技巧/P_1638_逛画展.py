"""
P1638 逛画展
https://www.luogu.com.cn/problem/P1638
Sliding Window
移動右端點的同時，維護窗口內的種類數，如果窗口內的畫種數為 m，則更新答案，並移動左端點
"""


def solve():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == n

    ans = (1, n)
    cnt = [0] * (m + 1)
    left, rem = 1, m
    for right, x in enumerate(A, start=1):
        cnt[x] += 1
        if cnt[x] == 1:
            rem -= 1
        while rem == 0:
            ans = min(ans, (left, right), key=lambda x: x[1] - x[0])
            y = A[left - 1]
            cnt[y] -= 1
            if cnt[y] == 0:
                rem += 1
            left += 1
    print(*ans)


if __name__ == "__main__":
    solve()

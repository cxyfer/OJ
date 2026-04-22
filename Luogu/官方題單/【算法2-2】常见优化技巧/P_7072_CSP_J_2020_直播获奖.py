"""
P7072 [CSP-J 2020] 直播获奖
https://www.luogu.com.cn/problem/P7072

注意到值域最大只有 600，因此可以維護一個 cnt 陣列，cnt[i] 表示分數為 i 的學生數量
由高到低枚舉分數，並計算累積人數，當累積人數 >= 當前人數 * w / 100 時，則該分數為當前獲獎分數
"""


def solve():
    n, w = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == n

    ans = []
    mx = max(A)
    cnt = [0] * (mx + 1)
    for i, x in enumerate(A, start=1):
        cnt[x] += 1
        s = 0
        tgt = max(1, i * w // 100)
        for score in range(mx, -1, -1):
            s += cnt[score]
            if s >= tgt:
                ans.append(score)
                break
    print(*ans)


if __name__ == "__main__":
    solve()

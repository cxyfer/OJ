"""
P2882 [USACO07MAR] Face The Right Way G
https://www.luogu.com.cn/problem/P2882
差分

本題的正確做法是枚舉所有可能的 k 值，然後計算所需要的操作次數，最後取最小的操作次數以及最小的 k 值。

有一種錯誤做法是從大到小找到第一個滿足題意的 k 值，但這種做法是錯誤的，只是數據有些問題導致此錯誤作法可以通過。
事實上是不滿足當 k 越大時操作次數越小的性質的，例如以下測資應該得到 `1 4`，但 `solve_wrong` 會得到 `2 7`

```text
10
B
F
B
F
B
F
F
F
F
B
```
"""


def solve_right():
    n = int(input())
    A = [0 if input().strip() == "F" else 1 for _ in range(n)]

    # 當 k = 1 時，每個都能個別翻轉，因此必定有解
    ans = (1, n)

    for k in range(1, n + 1):
        res = s = 0
        diff = [0] * (n + 1)
        for i in range(n):
            s ^= diff[i]
            if A[i] ^ s == 1:
                if i + k <= n:
                    res += 1
                    s ^= 1
                    diff[i + k] ^= 1
                else:
                    break
        else:
            ans = min(ans, (k, res), key=lambda x: (x[1], x[0]))
    print(*ans)


def solve_wrong():
    n = int(input())
    A = [0 if input().strip() == "F" else 1 for _ in range(n)]

    # 從大到小找到第一個滿足題意的 k 值（實際上是錯誤的）
    for k in range(n, 0, -1):
        ans = s = 0
        diff = [0] * (n + 1)
        for i in range(n):
            s ^= diff[i]
            if A[i] ^ s == 1:
                if i + k <= n:
                    ans += 1
                    s ^= 1
                    diff[i + k] ^= 1
                else:
                    break
        else:
            print(k, ans)
            break


# solve = solve_right
solve = solve_wrong


if __name__ == "__main__":
    solve()

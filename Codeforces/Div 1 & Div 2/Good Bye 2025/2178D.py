def solve():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))

    if 2 * m > n:
        print(-1)
        return

    idxs = list(range(n))
    idxs.sort(key=lambda idx: A[idx])
    
    ans = []
    if m > 0:
        # 多餘精靈 [0, n-2m): 讓他們自殺，每隻攻擊右邊更強的精靈
        ans.extend([(idxs[i], idxs[i + 1]) for i in range(n - 2 * m)])
        # 存活者 [n-m, n) 攻擊目標精靈 [n-2m, n-m)，存活者生存，目標死亡
        ans.extend([(idxs[n - m + i], idxs[n - 2 * m + i]) for i in range(m)])
    else:  # 所有人同歸於盡
        dmg = sum(A) - A[idxs[-1]]
        # 若總傷害不足以殺死最強者，則無解
        if dmg < A[idxs[-1]]:
            print(-1)
            return
        # 目標：讓倒數第二強的精靈與最強者同歸於盡
        # 先預留倒數第二強的攻擊力，作為最後一擊
        dmg -= A[idxs[-2]]
        # 若傷害溢出，則消耗多餘傷害
        i = 0
        while i < n - 2 and dmg >= A[idxs[-1]]:
            u, v = idxs[i], idxs[i + 1]
            ans.append((u, v))
            dmg -= A[u]
            i += 1
        # 剩餘精靈（包含倒數第二強）全部攻擊最強者，累積傷害直到它被擊殺
        for j in range(i, n - 1):
            ans.append((idxs[j], idxs[-1]))

    print(len(ans))
    for u, v in ans:
        print(u + 1, v + 1)

    def check():
        res = n
        hp = A[:]
        vis = [False] * n
        for u, v in ans:
            if vis[u] or hp[u] <= 0:
                return False
            vis[u] = True
            hp[v] -= A[u]
            if hp[v] <= 0:
                res -= 1
            hp[u] -= A[v]
            if hp[u] <= 0:
                res -= 1
        return res == m
    # assert check()

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
def solve():
    n, x, y = map(int, input().split())
    s = input()
    P = list(map(int, input().split()))
    assert len(P) == n

    # 1. 檢查總人數是否足夠覆蓋所有選區的最低要求
    if x + y < sum(P):
        print("NO")
        return

    # 2. 計算勝者所需的最小票數
    # cnt[0] 累積 A 當勝者時的最小需求, cnt[1] 累積 B 當勝者時的最小需求
    cnt = [0, 0] 
    for p, ch in zip(P, s):
        c = ord(ch) - ord('0')
        cnt[c] += (p >> 1) + 1

    # 檢查該黨持有的總票數 x 或 y 是否滿足其作為勝者的最小需求
    if x < cnt[0] or y < cnt[1]:
        print("NO")
        return

    # 檢查能否分配剩餘票數
    if cnt[0] and cnt[1] or cnt[0] and x >= y + n or cnt[1] and y >= x + n:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
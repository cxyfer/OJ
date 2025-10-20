"""
C-小彩的字符串交换
https://ac.nowcoder.com/acm/contest/119273/C

腦筋急轉彎 (+ 滑動窗口)

如果字串中沒有包含 '1', '2', '3' 中的任意一個，則一定無法交換。
否則必有兩個不同字元相鄰，這時將另一個字元交換到這兩個字元旁即可，最多需要 1 次交換；
若字串中已經包含連續的 "123" 排列，則不需要交換，可以用暴力枚舉或滑動窗口來檢查。
"""

def solve():
    n = int(input())
    s = input().strip()
    assert n == len(s)
    
    st = set(s)
    if len(st) != 3:
        print(-1)
        return
    cnt = [0] * 3
    for r, ch in enumerate(s):
        cnt[ord(ch) - ord('1')] += 1
        if r > 2:
            cnt[ord(s[r - 3]) - ord('1')] -= 1
        if cnt[0] == cnt[1] == cnt[2]:
            print(0)
            return
    print(1)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
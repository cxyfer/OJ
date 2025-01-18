import sys

input = sys.stdin.readline
print = sys.stdout.write

T = int(input())

"""
    令奇數為正數，偶數為負數
    所求為前綴和為0
    避免被卡hash，直接用str(s)來存
    https://codeforces.com/blog/entry/121908
"""
ans = []
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    flag = False
    s = 0
    seen = set([str(s)]) # 直接用int會被卡hash
    for i, x in enumerate(A):
        s += x if not (i & 1) else -x
        if str(s) in seen:
            flag = True
            break
        seen.add(str(s))
    ans.append("YES" if flag else "NO")
    # print("YES" if flag else "NO")
print("\n".join(ans))

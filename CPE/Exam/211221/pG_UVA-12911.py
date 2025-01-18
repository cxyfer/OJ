"""
    Half Enumeration / Meet in the Middle
    分成兩半，改成維護一個 list，分別考慮不使用新元素/使用新元素的情況
    並用 dict 來記錄每個子集和出現的次數，最後再將兩邊的 dict 進行配對，計算答案。
    這樣的做法可以將時間複雜度降到 O(2^(n/2))，適用於 n <= 40 的情況。
    Python 會 TLE ，必需用 C++ 才能 AC 。
"""
from collections import Counter

while True:
    try:
        n, target = map(int, input().split())
        arr = list(map(int, input().split()))
    except EOFError:
        break
    if n == 1:
        print(1 if arr[0] == target else 0)
        continue
    arr.sort()
    n1, n2 = n // 2, n - n // 2
    s1 = []
    for i in range(n1):
        s1 = s1 + [s + arr[i] for s in s1] + [arr[i]]
    cnt1 = Counter(s1)
    s2 = []
    for i in range(n1, n):
        s2 = s2 + [s + arr[i] for s in s2] + [arr[i]]
    cnt2 = Counter(s2)
    ans = 0
    for k, v in cnt1.items():
        ans += v * cnt2[target - k]
    ans += cnt1[target] + cnt2[target] # consider only one side
    print(ans)
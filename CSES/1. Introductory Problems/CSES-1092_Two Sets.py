"""
    Greedy
    先算出 [1, n] 的和 s，如果 s 是奇數，則無解；否則可以分成兩個和為 s//2 的集合。
    由大到小枚舉每個數字，如果加上這個數字後和不超過 s//2，則加入第一個集合，否則加入第二個集合。
    最後輸出兩個集合。
"""
n = int(input())
s = n * (n + 1) // 2 # sum of n numbers
s1 = s2 = s // 2
res1, res2 = [], []

if s & 1:
    print("NO")
else:
    for x in range(n, 0, -1):
        if s1 - x >= 0:
            res1.append(x)
            s1 -= x
        else:
            res2.append(x)
            s2 -= x
    print("YES")
    print(len(res1))
    print(*res1)
    print(len(res2))
    print(*res2)
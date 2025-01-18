"""
    二分答案 + 分組循環

    每組內的距離皆 <= m ，若奇數數量的組超過 1 ，則無法配對
"""
t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()

    def check(m):
        i = 0
        cnt = 0
        while i < n:
            j = i + 1
            while j < n and A[j] - A[j - 1] <= m:
                j += 1
            if (j - i) & 1:
                cnt += 1
            i = j
        return cnt <= 1
    
    left, right = 1, 10 ** 18 + 5
    while left <= right:
        mid = (left + right) >> 1
        if check(mid):
            right = mid - 1
        else:
            left = mid + 1
    print(left)
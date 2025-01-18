from collections import Counter
t = int(input())
"""
    質因數分解
"""
for case in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    cnt = Counter()
    for num in nums:
        # Start of factorization
        """
        prime =  2
        while num > 1:
            if num % prime == 0:
                num //= prime
                cnt[prime] += 1
            else:
                prime += 1
        """
        if num == 1:
            continue
        while num % 2 == 0:
            cnt[2] += 1
            num //= 2
        prime = 3
        while prime * prime <= num:  # 跳二
            while num % prime == 0:
                cnt[prime] += 1
                num //= prime
            prime += 2
        if num > 1:
            cnt[num] += 1
        # End of factorization
            
    ans = "YES"
    for key, value in cnt.items():
        if value % n != 0:
            ans = "NO"
            break
    print(ans)


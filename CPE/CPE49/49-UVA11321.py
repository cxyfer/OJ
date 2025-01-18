while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        print("0 0")
        break
    nums = [int(input()) for _ in range(N)]
    # 1. 餘數(注意負數的餘數是負數) 2. 奇數在前偶數在後 3. 奇數由大到小 偶數由小到大
    nums.sort(key=lambda x: (x % M if x >= 0 else -(abs(x) % M), 1 - x & 1, -x if x & 1 else x))
    print(N, M)
    for x in nums:
        print(x)
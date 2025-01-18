"""
    # 數學
    找中位數，計算所有數字與中位數的差的總和
    要注意輸入的第一位是數量，後面才是數字
"""
for _ in range(int(input())):
    n, *nums = map(int, input().split())
    nums.sort()
    print(sum(abs(x - nums[n//2]) for x in nums))

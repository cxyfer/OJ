""" CSES-1621 Distinct Numbers
    Sort / Hash Set
    這題的測資中有針對Hash Collision的，會讓 set 的時間複雜度從 O(1) 變成 O(n) ，因此會 TLE 。
    可以透過自訂 hash function 來解決，這邊是直接改用字串來作為 hash key
"""
n = int(input())
nums = list(map(int, input().split()))

def solve1():
    nums.sort()
    ans = 1
    for i in range(1, n):
        if nums[i] != nums[i-1]:
            ans += 1
    print(ans)

def solve2():
    hash_set = set()
    for num in nums:
        hash_set.add(str(num)) # 改用字串來作為 hash key
    print(len(hash_set))

# solve1()
solve2()
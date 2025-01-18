import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

# class Solution:
#     def minChanges(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         diffs = []
#         mn1, mn2 = float('inf'), float('inf')
#         for i in range(n//2):
#             nums[i], nums[n-i-1] = min(nums[i], nums[n-i-1]), max(nums[i], nums[n-i-1])
#             a, b = nums[i], nums[n-i-1]
#             diffs.append(b - a)
#             mn1 = min(mn1, k - a)
#             mn2 = min(mn2, b)
        
#         min_diff, max_diff = min(diffs), max(diffs)
#         max_diff = min(max_diff, max(mn1, mn2))
#         ans = float('inf')
        
#         for x in range(min_diff, max_diff + 1):
#             cur = 0
#             for i in range(n//2):
#                 a, b = nums[i], nums[n-i-1]
#                 if b - a == x: # already good
#                     continue
#                 """
#                     只改一次的情況：
#                     - 把 b 改成 a + x
#                     - 把 a 改成 b - x

#                     兩個都改的情況：
#                     - 把 a 改成 0 且 把 b 改成 x
#                 """
#                 if a + x <= k or b - x >= 0: # x <= k - a or x <= b
#                     cur += 1
#                 elif x <= k:
#                     cur += 2
#                 else:
#                     break
#             else:
#                 ans = min(ans, cur)
#         return ans

# class Solution:
#     def minChanges(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         N = 10005
#         cnt0 = [0] * N # cnt0[i] 為不操作時，對應的數字絕對值差為 i 的數量
#         diffs1 = [0] * N # pre[i] 為操作一次後，對應的數字絕對值差為 i 的數量，diffs1[i] 為其差分陣列
#         diffs2 = [0] * N # pre[i] 為操作兩次後，對應的數字絕對值差為 i 的數量，diffs2[i] 為其差分陣列

#         for i in range(n//2):
#             nums[i], nums[n-i-1] = min(nums[i], nums[n-i-1]), max(nums[i], nums[n-i-1])
#             a, b = nums[i], nums[n-i-1]
#             cnt0[b - a] += 1
#             # 考慮操作一次後可以得到的絕對值差範圍
#             intervals1 = []
#             intervals1.append([max(k - a, 0), b - a]) if b > k else intervals1.append([b - a, k - a]) # 把 b 改成 k (變小/變大)
#             intervals1.append([b - a, b]) # 把 a 改成 0 (變小)
#             intervals1.append([max(b - k, 0), b - a] if k > a else [b - a, b - k]) # 把 a 改成 k (變大/變小)
#             intervals1.append([a - min(a, k), a]) # 把 b 改成 0 (變小)
#             intervals1.sort(key = lambda x: x[0])
#             print(intervals1)
#             exit()
#             # merge intervals
#             last = None
#             for a, b in intervals1:
#                 if last is None:
#                     last = [a, b]
#                 elif last[1] >= a:
#                     last[1] = max(last[1], b)
#                 else:
#                     diffs1[last[0]] += 1
#                     diffs1[a] -= 1
#                     last = [a, b]


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)

        mp = defaultdict(list)
        diffs = [0] * (n // 2)
        for i in range(n // 2):
            a, b = min(nums[i], nums[n - i - 1]), max(nums[i], nums[n - i - 1])
            mx = max(b, k - a)
            mp[b - a].append(mx)
            diffs[i] = mx
        
        ans = n
        diffs.sort()
        for k, vals in mp.items():
            vals.sort()
            idx = bisect_left(diffs, k)
            cur = idx * 2 + (n // 2 - idx)
            for y in vals:
                if y < k:
                    cur -= 2
                else:
                    cur -= 1
            ans = min(ans, cur)
        return ans
            
#   class Solution {
# public:
#     int minChanges(std::vector<int>& nums, int k) {
#         std::map<int, std::vector<int>> m;
#         std::vector<int> v;
 
#         for (int i = 0; i < nums.size() / 2; ++i) {
#             int a = nums[i];
#             int b = nums[nums.size() - i - 1];
#             int diff = std::abs(a - b);

#              int X = std::max({a, b, k - a, k - b});

#              m[diff].push_back(X);
#             v.push_back(X);
#         }

#         int ans = nums.size();  
#         std::sort(v.begin(), v.end());

#         for (const auto& [diff, values] : m) {
#             int T = std::lower_bound(v.begin(), v.end(), diff) - v.begin();
#             T = T * 2 + (nums.size() / 2 - T);

#             for (const auto& X : values) {
#                 if (X < diff) {
#                     T -= 2;
#                 } else {
#                     T -= 1;
#                 }
#             }

#             ans = std::min(ans, T);
#         }

#         return ans;
#     }
# };
    
sol = Solution()
print(sol.minChanges([1,0,1,2,4,3], 4)) # 2
print(sol.minChanges([0,1,2,3,3,6,5,4], 6)) # 2
print(sol.minChanges([0,11,8,9,9,4,10,8,5,7,0,2,11,12,6,5], 12)) # 6
print(sol.minChanges([9,2,7,7,8,9,1,5,1,9,4,9,4,7], 9)) # 4
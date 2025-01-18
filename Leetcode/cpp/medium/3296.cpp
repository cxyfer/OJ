/*
 * @lc app=leetcode.cn id=3296 lang=cpp
 *
 * [3296] 移山所需的最少秒数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    long long minNumberOfSeconds(int mountainHeight, vector<int>& workerTimes) {
        function<bool(long long)> check = [&](long long m) -> bool {
            long long tot = 0;
            for (int t : workerTimes) {
                long long x = (-1 + sqrt(1 + 8 * m / t)) / 2;
                tot += x;
            }
            return tot >= mountainHeight;
        };
        long long left = 0, right = 1e18;
        while (left <= right) {
            long long mid = left + (right - left) / 2;
            if (check(mid)) right = mid - 1;
            else left = mid + 1;
        }
        return left;
    }
};
// @lc code=end

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def check(m: int) -> bool:
            tot = 0 # 降低的總高度
            for t in workerTimes: # 枚舉每個工人
                # 計算工人可以降低的高度
                """
                    t + 2t + 3t + ... + xt <= m
                    t * (x * (x + 1) // 2) <= m
                    x^2 + x - (2m / t) <= 0
                    x <= (-1 + sqrt(1 + 8 * m / t)) / 2
                """
                x = (-1 + math.isqrt(int(1 + 8 * m // t))) // 2
                tot += x
            return tot >= mountainHeight
        
        left, right = 0, 1e18
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
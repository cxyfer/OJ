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
class Solution1 {
public:
    long long minNumberOfSeconds(int mountainHeight, vector<int>& workerTimes) {
        int n = workerTimes.size();
        auto check = [&](long long m) -> bool {
            long long tot = 0;
            for (int t : workerTimes) {
                tot += (-1 + sqrt(1 + 8 * m / t)) / 2;
                if (tot >= mountainHeight) return true;
            }
            return false;
        };

        long long h = ceil(double(mountainHeight) / n);
        long long left = 0;
        long long right = ranges::max(workerTimes) * h * (h + 1) / 2;
        while (left <= right) {
            long long mid = left + (right - left) / 2;
            if (check(mid)) right = mid - 1;
            else left = mid + 1;
        }
        return left;
    }
};

class Solution2 {
public:
    long long minNumberOfSeconds(int mountainHeight, vector<int>& workerTimes) {
        priority_queue<array<long long, 3>, vector<array<long long, 3>>, greater<>> pq;
        for (int t : workerTimes) {
            pq.emplace(array<long long, 3>{t, t, 1});
        }

        long long ans = 0;
        while (mountainHeight--) {
            auto [t, d, m] = pq.top(); pq.pop();
            m += 1;
            ans = t;
            pq.push({t + d * m, d, m});
        }
        return ans;
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end
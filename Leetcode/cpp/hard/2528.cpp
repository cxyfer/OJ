/*
 * @lc app=leetcode.cn id=2528 lang=cpp
 * @lcpr version=30204
 *
 * [2528] 最大化城市的最小电量
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    long long maxPower(vector<int>& stations, int d, int k) {
        int n = stations.size();

        auto check = [&](long long mid) -> bool {
            vector<long long> diff(n + 1);
            long long s = accumulate(stations.begin(), stations.begin() + d, 0LL);
            long long cnt = 0;
            for (int i = 0; i < n; ++i) {
                if (i + d < n) s += stations[i + d];
                if (i - d - 1 >= 0) s -= stations[i - d - 1];
                s += diff[i];
                if (s < mid) {
                    long long add = mid - s;
                    cnt += add;
                    if (cnt > k) return false;
                    s += add;
                    diff[min(n, i + 2 * d + 1)] -= add;
                }
            }
            return true;
        };

        long long left = *min_element(stations.begin(), stations.end());
        long long right = accumulate(stations.begin(), stations.end(), 0LL) + k;
        while (left <= right) {
            long long mid = left + (right - left) / 2;
            if (check(mid)) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return right;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,2,4,5,0]\n1\n2\n
// @lcpr case=end

// @lcpr case=start
// [4,4,4,4]\n0\n3\n
// @lcpr case=end

 */


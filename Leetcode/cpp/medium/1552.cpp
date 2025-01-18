/*
 * @lc app=leetcode.cn id=1552 lang=cpp
 *
 * [1552] 两球之间的磁力
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int maxDistance(vector<int>& position, int m) {
        int n = position.size();
        sort(position.begin(), position.end());

        auto check = [&](int d) {
            int cnt = 1;
            int pre = position[0];
            for (int i = 1; i < n; ++i) {
                if (position[i] - pre >= d) {
                    cnt++;
                    pre = position[i];
                }
            }
            return cnt >= m;
        };

        int left = 0, right = position[n - 1] - position[0];
        while (left <= right) {
            int mid = (left + right) / 2;
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
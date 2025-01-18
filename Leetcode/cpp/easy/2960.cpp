/*
 * @lc app=leetcode.cn id=2960 lang=cpp
 *
 * [2960] 统计已测试设备
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int countTestedDevices(vector<int>& batteryPercentages) {
        int ans = 0;
        for (int x : batteryPercentages) {
            if (x - ans > 0) ans++;
        }
        return ans;
    }
};
// @lc code=end


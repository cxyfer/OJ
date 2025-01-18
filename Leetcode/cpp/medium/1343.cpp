/*
 * @lc app=leetcode.cn id=1343 lang=cpp
 *
 * [1343] 大小为 K 且平均值大于等于阈值的子数组数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int numOfSubarrays(vector<int>& arr, int k, int threshold) {
        int n = arr.size();
        int ans = 0, cur = 0, target = k * threshold;
        for (int i = 0; i < n; i++) {
            cur += arr[i];
            if (i < k - 1) continue;
            ans += cur >= target;
            cur -= arr[i - k + 1];
        }
        return ans;
    }
};
// @lc code=end


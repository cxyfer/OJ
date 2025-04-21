/*
 * @lc app=leetcode.cn id=2145 lang=cpp
 * @lcpr version=30204
 *
 * [2145] 统计隐藏数组数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int numberOfArrays(vector<int>& differences, int lower, int upper) {
        int n = differences.size();
        long long s = lower, mn = lower, mx = lower;
        for (int x : differences) {
            s += x;
            mn = min(mn, s);
            mx = max(mx, s);
        }
        return max(0LL, (upper - (mx + lower - mn)) + 1);
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,-3,4]\n1\n6\n
// @lcpr case=end

// @lcpr case=start
// [3,-4,5,1,-2]\n-4\n5\n
// @lcpr case=end

// @lcpr case=start
// [4,-7,2]\n3\n6\n
// @lcpr case=end

 */


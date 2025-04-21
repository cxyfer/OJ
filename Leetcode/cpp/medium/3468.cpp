/*
 * @lc app=leetcode.cn id=3468 lang=cpp
 * @lcpr version=30204
 *
 * [3468] 可行数组的数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int countArrays(vector<int>& original, vector<vector<int>>& bounds) {
        int lo = INT_MIN, hi = INT_MAX;
        for (int i = 0; i < original.size(); i++) {
            int d = original[i] - original[0];
            hi = min(hi, bounds[i][1] - d);
            lo = max(lo, bounds[i][0] - d);
        }
        return max(0, hi - lo + 1);
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,2,3,4]\n[[1,2],[2,3],[3,4],[4,5]]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4]\n[[1,10],[2,9],[3,8],[4,7]]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,1,2]\n[[1,1],[2,3],[3,3],[2,3]]\n
// @lcpr case=end

 */


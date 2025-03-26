/*
 * @lc app=leetcode.cn id=2033 lang=cpp
 * @lcpr version=30204
 *
 * [2033] 获取单值网格的最小操作数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int minOperations(vector<vector<int>>& grid, int x) {
        vector<int> arr;
        for (const auto& row : grid)
            arr.insert(arr.end(), row.begin(), row.end());
        int idx = arr.size() / 2;
        nth_element(arr.begin(), arr.begin() + idx, arr.end());
        int median = arr[idx];
        int ans = 0;
        for (int v : arr) {
            if (abs(v - median) % x != 0) return -1;
            ans += abs(v - median) / x;
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [[2,4],[6,8]]\n2\n
// @lcpr case=end

// @lcpr case=start
// [[1,5],[2,3]]\n1\n
// @lcpr case=end

// @lcpr case=start
// [[1,2],[3,4]]\n2\n
// @lcpr case=end

 */


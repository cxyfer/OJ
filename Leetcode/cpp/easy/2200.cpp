/*
 * @lc app=leetcode.cn id=2200 lang=cpp
 * @lcpr version=30204
 *
 * [2200] 找出数组中的所有 K 近邻下标
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<int> findKDistantIndices(vector<int>& nums, int key, int k) {
        int n = nums.size();
        queue<int> pos;
        for (int i = 0; i < n; i++)
            if (nums[i] == key)
                pos.push(i);
        vector<int> ans;
        for (int i = 0; i < n; i++) {
            while (!pos.empty() && i > pos.front() + k)
                pos.pop();
            if (pos.empty()) break;
            if (i >= pos.front() - k)
                ans.push_back(i);
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [3,4,9,1,3,9,5]\n9\n1\n
// @lcpr case=end

// @lcpr case=start
// [2,2,2,2,2]\n2\n2\n
// @lcpr case=end

 */


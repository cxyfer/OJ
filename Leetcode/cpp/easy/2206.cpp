/*
 * @lc app=leetcode.cn id=2206 lang=cpp
 * @lcpr version=30204
 *
 * [2206] 将数组划分成相等数对
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    bool divideArray(vector<int>& nums) {
        int n = nums.size() / 2;
        int ans = 0;
        vector<bool> vis(501, false);
        for (int x : nums) {
            ans += vis[x];
            vis[x] = !vis[x];
        }
        return ans == n;
    }
};

class Solution2 {
public:
    bool divideArray(vector<int>& nums) {
        vector<bool> vis(501, false);
        for (int x : nums) vis[x] = !vis[x];
        return all_of(vis.begin(), vis.end(), [](bool x) { return x == false; });
    }
};

class Solution3 {
public:
    bool divideArray(vector<int>& nums) {
        unordered_set<int> vis;
        for (int x : nums) {
            if (vis.count(x)) vis.erase(x);
            else vis.insert(x);
        }
        return vis.empty();
    }
};

class Solution : public Solution1 {};
// class Solution : public Solution2 {};
// class Solution : public Solution3 {};
// @lc code=end

/*
// @lcpr case=start
// [3,2,3,2,2,2]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4]\n
// @lcpr case=end

 */


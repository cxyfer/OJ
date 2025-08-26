/*
 * @lc app=leetcode.cn id=113 lang=cpp
 * @lcpr version=30204
 *
 * [113] 路径总和 II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};
// @lc code=start
class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int>> ans;
        vector<int> path;
        auto dfs = [&](this auto&& dfs, TreeNode* node, int targetSum) -> void {
            if (node == nullptr) return;
            path.push_back(node->val);
            targetSum -= node->val;
            if (node->left == nullptr && node->right == nullptr && targetSum == 0)
                ans.push_back(path);
            dfs(node->left, targetSum);
            dfs(node->right, targetSum);
            path.pop_back();
            return;
        };
        dfs(root, targetSum);
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [5,4,8,11,null,13,4,7,2,null,null,5,1]\n22\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3]\n5\n
// @lcpr case=end

// @lcpr case=start
// [1,2]\n0\n
// @lcpr case=end

 */


/*
 * @lc app=leetcode.cn id=124 lang=cpp
 *
 * [124] 二叉树中的最大路径和
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxPathSum(TreeNode* root) {
        int ans = INT_MIN;
        auto dfs = [&](auto&& dfs, TreeNode* root) -> int {
            if (root == nullptr) return 0;
            int left = max(dfs(dfs, root->left), 0);
            int right = max(dfs(dfs, root->right), 0);
            ans = max(ans, root->val + left + right);
            return root->val + max(left, right);
        };
        dfs(dfs, root);
        return ans;
    }
};
// @lc code=end


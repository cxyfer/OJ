/*
 * @lc app=leetcode.cn id=687 lang=cpp
 *
 * [687] 最长同值路径
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
    int longestUnivaluePath(TreeNode* root) {
        int ans = 0;
        auto dfs = [&](auto&& dfs, TreeNode* node) -> int {
            if (!node) return 0;
            int left = dfs(dfs, node->left) + 1;
            int right = dfs(dfs, node->right) + 1;
            if (node->left == nullptr || node->left->val != node->val) left = 0;
            if (node->right == nullptr || node->right->val != node->val) right = 0;
            ans = max(ans, left + right);
            return max(left, right);
        };
        dfs(dfs, root);
        return ans;
    }
};
// @lc code=end


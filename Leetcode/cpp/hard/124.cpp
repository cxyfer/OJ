/*
 * @lc app=leetcode.cn id=124 lang=cpp
 *
 * [124] 二叉树中的最大路径和
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int maxPathSum(TreeNode* root) {
        int ans = INT_MIN / 2;
        auto dfs = [&](this auto&& dfs, TreeNode* root) -> int {
            if (root == nullptr) return 0;
            int left = max(dfs(root->left), 0);    // 不選負數
            int right = max(dfs(root->right), 0);  // 不選負數
            ans = max(ans, root->val + left + right);
            return root->val + max(left, right);   // 到葉子的最長路徑
        };
        dfs(root);
        return ans;
    }
};
// @lc code=end


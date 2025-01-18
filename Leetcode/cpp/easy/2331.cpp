/*
 * @lc app=leetcode.cn id=2331 lang=cpp
 *
 * [2331] 计算布尔二叉树的值
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
    bool evaluateTree(TreeNode* root) {
        // if (root->left == nullptr && root->right == nullptr) {
        if (root->left == nullptr) {
            return root->val;
        }
        if (root->val == 3) return evaluateTree(root->left) && evaluateTree(root->right);
        else return evaluateTree(root->left) || evaluateTree(root->right);
    }
};
// @lc code=end


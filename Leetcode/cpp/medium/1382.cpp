/*
 * @lc app=leetcode.cn id=1382 lang=cpp
 *
 * [1382] 将二叉搜索树变平衡
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
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
// @lc code=start
class Solution {
public:
    vector<int> nums;

    TreeNode* balanceBST(TreeNode* root) {
        inorder(root);
        return build(0, nums.size() - 1);
    }

    // Inorder traversal to get the sorted list of values
    void inorder(TreeNode* node) {
        if (node == nullptr) return;
        inorder(node->left);
        nums.push_back(node->val);
        inorder(node->right);
    }

    // Build the balanced BST from the sorted list
    TreeNode* build(int l, int r) {
        if (l > r) return nullptr;
        int mid = (l + r) / 2;
        TreeNode* node = new TreeNode(nums[mid]);
        node->left = build(l, mid - 1);
        node->right = build(mid + 1, r);
        return node;
    }
};
// @lc code=end
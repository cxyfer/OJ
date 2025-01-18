/*
 * @lc app=leetcode id=2236 lang=cpp
 * @lcpr version=30111
 *
 * [2236] Root Equals Sum of Children
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
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
    bool checkTree(TreeNode* root) {
        return root->val == (root->left->val + root->right->val);
    }
};
// @lc code=end



/*
// @lcpr case=start
// [10,4,6]\n
// @lcpr case=end

// @lcpr case=start
// [5,3,1]\n
// @lcpr case=end

 */


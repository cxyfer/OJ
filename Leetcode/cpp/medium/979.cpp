/*
 * @lc app=leetcode.cn id=979 lang=cpp
 *
 * [979] 在二叉树中分配硬币
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
    int ans;
    pair<int, int> dfs1(TreeNode* root) {
        if (root == nullptr) return {0, 0};
        pair<int, int> res = {1, root->val}; // (need, have)
        pair<int, int> left = dfs1(root->left), right = dfs1(root->right);
        res.first += left.first + right.first;
        res.second += left.second + right.second;
        ans += abs(res.first - res.second); 
        return res;
    }
    int dfs2(TreeNode* root) { // 正數表示多餘的硬幣，負數表示缺少的硬幣
        if (root == nullptr) return 0;
        int left = dfs2(root->left), right = dfs2(root->right);
        ans += abs(left) + abs(right); // 要往上拿回/往下給多少硬幣
        return root->val + left + right - 1;
    }
    int distributeCoins(TreeNode* root) {
        ans = 0;
        dfs1(root);
        // dfs2(root);
        return ans;
    }
};
// @lc code=end


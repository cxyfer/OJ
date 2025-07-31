/*
 * @lc app=leetcode.cn id=652 lang=cpp
 * @lcpr version=30204
 *
 * [652] 寻找重复的子树
 */

// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right)
        : val(x), left(left), right(right) {}
};
// @lc code=start
#include <ranges>

class Solution {
public:
    vector<TreeNode*> findDuplicateSubtrees(TreeNode* root) {
        unordered_map<string, TreeNode*> mp;
        unordered_map<string, int> cnt;
        auto dfs = [&](this auto&& dfs, TreeNode* node) -> string {
            if (!node) return "";
            string expr = to_string(node->val) + "(" + dfs(node->left) + ")" +
                          "(" + dfs(node->right) + ")";
            mp[expr] = node;
            cnt[expr]++;
            return expr;
        };
        dfs(root);
        return cnt | views::filter([](const auto& p) { return p.second > 1; }) |
               views::transform([&](const auto& p) { return mp[p.first]; }) |
               ranges::to<vector<TreeNode*>>();
    }
};
// @lc code=end

/*
// @lcpr case=start
// [1,2,3,4,null,2,4,null,null,4]\n
// @lcpr case=end

// @lcpr case=start
// [2,1,1]\n
// @lcpr case=end

// @lcpr case=start
// [2,2,2,3,null,3,null]\n
// @lcpr case=end

 */

/*
 * @lc app=leetcode.cn id=1110 lang=cpp
 *
 * [1110] 删点成林
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
    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
        vector<TreeNode*> ans;
        unordered_set<int> to_delete_set(to_delete.begin(), to_delete.end());
        function<TreeNode*(TreeNode*, bool)> dfs = [&](TreeNode* root, bool is_root) -> TreeNode* {
            if (!root) return nullptr;
            if (to_delete_set.count(root->val)) {
                dfs(root->left, true);
                dfs(root->right, true);
                return nullptr;
            } else {
                if (is_root) ans.push_back(root);
                root->left = dfs(root->left, false);
                root->right = dfs(root->right, false);
                return root;
            }
        };
        dfs(root, true);
        return ans;
    }
};
// @lc code=end
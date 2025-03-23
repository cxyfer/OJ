/*
 * @lc app=leetcode.cn id=199 lang=cpp
 * @lcpr version=30204
 *
 * [199] 二叉树的右视图
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
class Solution1 {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> ans;
        queue<TreeNode*> q;
        if (root != nullptr) q.push(root);
        while (!q.empty()) {
            int ln = q.size();
            TreeNode* u;
            for (int i = 0; i < ln; i++) {
                u = q.front(); q.pop();
                if (u->left != nullptr) q.push(u->left);
                if (u->right != nullptr) q.push(u->right);
            }
            ans.push_back(u->val);
        }
        return ans;
    }
};

class Solution2 {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> ans;
        auto dfs = [&](auto&& dfs, TreeNode* node, int depth) -> void {
            if (node == nullptr) return;
            if (depth == ans.size()) ans.push_back(node->val);
            dfs(dfs, node->right, depth + 1);
            dfs(dfs, node->left, depth + 1);
            return;
        };
        dfs(dfs, root, 0);
        return ans;
    }
};

using Solution = Solution1;
// using Solution = Solution2;
// @lc code=end



/*
// @lcpr case=start
// [1,2,3,null,5,null,4]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4,null,null,null,5]\n
// @lcpr case=end

// @lcpr case=start
// [1,null,3]\n
// @lcpr case=end

// @lcpr case=start
// []\n
// @lcpr case=end

 */


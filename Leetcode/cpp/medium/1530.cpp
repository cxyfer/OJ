/*
 * @lc app=leetcode.cn id=1530 lang=cpp
 *
 * [1530] 好叶子节点对的数量
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
    int countPairs(TreeNode* root, int distance) {
        int ans = 0;
        function<vector<int>(TreeNode*)> dfs = [&](TreeNode* node) -> vector<int> {
            vector<int> cnt(distance + 1);
            if (!node->left && !node->right) {
                cnt[0] = 1;
                return cnt;
            }
            vector<int> lcnt = node->left ? dfs(node->left) : vector<int>(distance + 1);
            vector<int> rcnt = node->right ? dfs(node->right) : vector<int>(distance + 1);
            for (int i = 0; i <= distance; i++) {
                for (int j = 0; j <= distance - i - 2; j++) {
                    ans += lcnt[i] * rcnt[j];
                }
            }
            for (int i = 0; i < distance; i++) {
                cnt[i + 1] = lcnt[i] + rcnt[i];
            }
            return cnt;
        };
        dfs(root);
        return ans;
    }
};
// @lc code=end
/*
 * @lc app=leetcode id=1028 lang=cpp
 *
 * [1028] Recover a Tree From Preorder Traversal
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// Definition for a binary tree node.
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
    TreeNode* recoverFromPreorder(string traversal) {
        int n = traversal.size(), i = 0;
        vector<TreeNode*> st;
        while (i < n) {
            // 計算深度，即 '-' 的數量
            int lvl = 0;
            while (i < n && traversal[i] == '-') {
                lvl++;
                i++;
            }
            // 計算節點值
            int val = 0;
            while (i < n && traversal[i] >= '0' && traversal[i] <= '9') {
                val = val * 10 + (traversal[i] - '0');
                i++;
            }
            // 創建新節點
            TreeNode* node = new TreeNode(val);

            // 如果堆疊不為空，則代表非根節點
            if (!st.empty()) {
                // 調整堆疊大小，確保堆疊頂端節點為當前節點的父節點
                if (st.size() > lvl)
                    st.erase(st.begin() + lvl, st.end());
                // 根據題意，若一個節點有子節點，則先左子節點，再右子節點
                if (st.back()->left == nullptr)
                    st.back()->left = node;
                else
                    st.back()->right = node;
            }
            // 將當前節點壓入堆疊
            st.push_back(node);
        }
        // 返回根節點
        return st[0];
    }
};
// @lc code=end


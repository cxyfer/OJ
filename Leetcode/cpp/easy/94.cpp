/*
 * @lc app=leetcode.cn id=94 lang=cpp
 *
 * [94] 二叉树的中序遍历
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
    /*
        1. Recursion
        2. Iteration + Stack
        3. Morris Traversal
            SC: O(1)
    */
    vector<int> inorderTraversal(TreeNode* root) {
        // return solve1(root);
        // return solve2(root);
        return solve3(root);
    }
    vector<int> solve1(TreeNode* root) {
        if (!root) return {};
        vector<int> left = inorderTraversal(root->left);
        vector<int> right = inorderTraversal(root->right);
        vector<int> res;
        res.insert(res.end(), left.begin(), left.end());
        res.push_back(root->val);
        res.insert(res.end(), right.begin(), right.end());
        return res;
    }
    vector<int> solve2(TreeNode* root) {
        vector<int> res;
        stack<TreeNode*> st;
        TreeNode* cur = root;
        while (cur || !st.empty()){
            while (cur){
                st.push(cur);
                cur = cur->left;
            }
            cur = st.top(); st.pop();
            res.push_back(cur->val);
            cur = cur->right;
        }
        return res;
    }
    vector<int> solve3(TreeNode* root) {
        vector<int> res;
        TreeNode *pre = nullptr; // predecessor 前驅節點，即左子樹中的最右節點

        while (root != nullptr) {
            if (root->left != nullptr) { // 存在左子樹
                pre = root->left;
                while (pre->right != nullptr && pre->right != root) { // 找到左子樹中的最右節點
                    pre = pre->right;
                }
                if (pre->right == nullptr) { // 左子樹還沒有被訪問過，遍歷左子樹
                    pre->right = root;
                    root = root->left;
                }
                else { // 左子樹已經訪問過，可以訪問當前節點了，並斷開 pre 指向 root 的指標
                    res.push_back(root->val); 
                    pre->right = nullptr;
                    root = root->right;
                }
            }
            else { // 不存在左子樹，直接訪問右子樹
                res.push_back(root->val);
                root = root->right;
            }
        }
        return res;
    }
};
// @lc code=end


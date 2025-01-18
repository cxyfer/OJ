/*
 * @lc app=leetcode.cn id=2196 lang=cpp
 *
 * [2196] 根据描述创建二叉树
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
struct TreeNode{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
// @lcpr-template-end
// @lc code=start

class DSU {
public:
    vector<int> pa;
    DSU(int n) {
        pa.resize(n);
        iota(pa.begin(), pa.end(), 0);
    }
    int find(int x) {
        return pa[x] == x ? x : pa[x] = find(pa[x]);
    }
    bool unionSet(int x, int y) {
        x = find(x), y = find(y);
        if (x == y) return false;
        pa[y] = x;
        return true;
    }
};

class Solution1 {
public:
    const int N = 1e5 + 5;
    TreeNode* createBinaryTree(vector<vector<int>>& descriptions) {
        DSU dsu(N);
        unordered_map<int, TreeNode*> mp;
        for (auto& desc : descriptions) {
            int u = desc[0], v = desc[1];
            bool is_left = desc[2];
            dsu.unionSet(u, v);
            if (!mp.count(u)) mp[u] = new TreeNode(u);
            if (!mp.count(v)) mp[v] = new TreeNode(v);
            if (is_left) mp[u]->left = mp[v];
            else mp[u]->right = mp[v];
        }
        int root = dsu.find(descriptions[0][0]);
        return mp[root];
    }
};

class Solution2 {
public:
    TreeNode* createBinaryTree(vector<vector<int>>& descriptions) {
        unordered_map<int, TreeNode*> mp;
        unordered_map<int, int> pa;
        for (auto& desc : descriptions) {
            int u = desc[0], v = desc[1];
            bool is_left = desc[2];
            pa[v] = u;
            if (!mp.count(u)) mp[u] = new TreeNode(u);
            if (!mp.count(v)) mp[v] = new TreeNode(v);
            if (is_left) mp[u]->left = mp[v];
            else mp[u]->right = mp[v];
        }
        int root = descriptions[0][0];
        while (pa.count(root)) root = pa[root];
        return mp[root];
    }
};

// class Solution : public Solution1 {};
class Solution : public Solution2 {};
// @lc code=end
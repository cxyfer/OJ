/*
 * @lc app=leetcode.cn id=1233 lang=cpp
 *
 * [1233] 删除子文件夹
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class TrieNode {
public:
    unordered_map<string, TrieNode*> child;
    int fid;
    TrieNode(): fid(-1) {}
    void insert(const string& path, int i) {
        TrieNode* node = this;
        stringstream ss(path);
        string p;
        while (getline(ss, p, '/')) {
            if (!node->child[p]) node->child[p] = new TrieNode();
            node = node->child[p];
        }
        node->fid = i;
    }
};

class Solution {
public:
    vector<string> removeSubfolders(vector<string>& folder) {
        TrieNode* root = new TrieNode();
        for (int i = 0; i < folder.size(); ++i) {
            root->insert(folder[i], i);
        }
        vector<string> ans;
        auto dfs = [&](auto&& dfs, TrieNode* node) {
            if (node->fid != -1) {
                ans.push_back(folder[node->fid]);
                return;
            }
            for (auto& [_, child] : node->child) dfs(dfs, child);
        };
        dfs(dfs, root);
        return ans;
    }
};
// @lc code=end


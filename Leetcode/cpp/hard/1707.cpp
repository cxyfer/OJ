/*
 * @lc app=leetcode.cn id=1707 lang=cpp
 * @lcpr version=30204
 *
 * [1707] 与数组中元素的最大异或值
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class TrieNode {
public:
    TrieNode* child[2];
    int min_val;
    TrieNode() {
        child[0] = child[1] = nullptr;
        min_val = INT_MAX;
    }
};

class Trie {
public:
    TrieNode* root;
    int B;
    Trie(int B = 30) {
        root = new TrieNode();
        this->B = B;
    }

    void insert(int x) {
        TrieNode* node = root;
        node->min_val = min(node->min_val, x);
        for (int i = B; i >= 0; i--) {
            int b = (x >> i) & 1;
            if (node->child[b] == nullptr) node->child[b] = new TrieNode();
            node = node->child[b];
            node->min_val = min(node->min_val, x);
        }
    }

    int max_xor(int x, int m) {
        TrieNode* node = root;
        if (node->min_val > m) return -1;
        int res = 0;
        for (int i = B; i >= 0; i--) {
            int b = (x >> i) & 1;
            if (node->child[b ^ 1] != nullptr && node->child[b ^ 1]->min_val <= m) {
                res |= (1 << i);
                node = node->child[b ^ 1];
            } else {
                node = node->child[b];
            }
        }
        return res;
    }
};

class Solution {
public:
    vector<int> maximizeXor(vector<int>& nums, vector<vector<int>>& queries) {
        Trie trie(30);
        for (int x : nums) trie.insert(x);
        vector<int> ans;
        for (auto& q : queries) ans.push_back(trie.max_xor(q[0], q[1]));
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [0,1,2,3,4]\n[[3,1],[1,3],[5,6]]\n
// @lcpr case=end

// @lcpr case=start
// [5,2,4,6,6,3]\n[[12,4],[8,1],[6,3]]\n
// @lcpr case=end

 */


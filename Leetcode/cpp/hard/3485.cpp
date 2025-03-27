/*
 * @lc app=leetcode.cn id=3485 lang=cpp
 * @lcpr version=30204
 *
 * [3485] Longest Common Prefix of K Strings After Removal
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Node {
public:
    int dep, cnt;
    unordered_map<char, Node*> child;

    Node(int d) : dep(d), cnt(0) {}
};

class Trie {
public:
    Node* root;

    Trie() {
        root = new Node(0);
    }

    void insert(const string& s) {
        Node* cur = root;
        for (char ch : s) {
            if (cur->child.find(ch) == cur->child.end())
                cur->child[ch] = new Node(cur->dep + 1);
            cur = cur->child[ch];
            cur->cnt += 1;
        }
    }
};

class Solution {
public:
    vector<int> longestCommonPrefix(vector<string>& words, int k) {
        Trie trie;
        for (const string& word : words) trie.insert(word);
        set<pair<int, Node*>> st;  // {depth, node}
        for (const string& word : words) {
            Node* cur = trie.root;
            for (char ch : word) {
                cur = cur->child[ch];
                if (cur->cnt >= k) st.insert({cur->dep, cur});
            }
        }

        auto calc = [&](const string& s) -> int {
            int res = 0;
            // Erase nodes of this path
            Node* cur = trie.root;
            for (char ch : s) {
                cur = cur->child[ch];
                if (cur->cnt >= k) st.erase({cur->dep, cur});
                if (cur->cnt >= k + 1) res = max(res, cur->dep);
            }

            // Find the longest common prefix
            if (!st.empty()) {
                auto [d, node] = *st.rbegin();
                res = max(res, d);
            }

            // Reinsert nodes of this path
            cur = trie.root;
            for (char ch : s) {
                cur = cur->child[ch];
                if (cur->cnt >= k) st.insert({cur->dep, cur});
            }
            return res;
        };

        vector<int> ans;
        for (const string& word : words) ans.push_back(calc(word));
        return ans;
    }
};
// @lc code=end
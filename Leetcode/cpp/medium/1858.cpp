/*
 * @lc app=leetcode id=1858 lang=cpp
 *
 * [1858] Longest Word With All Prefixes
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class TrieNode {
public:
    vector<TrieNode*> child;
    bool is_end;
    TrieNode() {
        child = vector<TrieNode*>(26, nullptr);
        is_end = false;
    }
};
class Solution {
public:
    string longestWord(vector<string>& words) {
        TrieNode* root = new TrieNode();
        for (string& word : words) {
            TrieNode* node = root;
            for (char ch : word) {
                int idx = ch - 'a';
                if (node->child[idx] == nullptr) {
                    node->child[idx] = new TrieNode();
                }
                node = node->child[idx];
            }
            node->is_end = true;
        }
        string ans = "";
        for (string& word : words) {
            TrieNode* node = root;
            bool valid = true;
            for (char ch : word) {
                int idx = ch - 'a';
                if (node->child[idx] == nullptr || !node->child[idx]->is_end) {
                    valid = false;
                    break;
                }
                node = node->child[idx];
            }
            if (valid && (word.length() > ans.length() || (word.length() == ans.length() && word < ans))) {
                ans = word;
            }
        }
        return ans;
    }
};
// @lc code=end

